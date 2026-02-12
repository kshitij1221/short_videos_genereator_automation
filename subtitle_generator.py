"""
Subtitle Generator - Integrated with config and logging
Generates subtitles using OpenAI Whisper
"""

import os
import subprocess
from pathlib import Path
import config
from logger import get_logger

logger = get_logger()

try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False
    logger.warning("Whisper not installed. Subtitle generation unavailable.")
    logger.info("Install with: pip install openai-whisper")


class SubtitleGenerator:
    def __init__(self, model_size=None):
        """
        Initialize subtitle generator
        
        Args:
            model_size (str): Whisper model size (uses config if None)
        """
        self.model_size = model_size or config.WHISPER_MODEL
        self.model = None
        
        if WHISPER_AVAILABLE:
            logger.info(f"Loading Whisper model ({self.model_size})...")
            logger.info("(First time will download the model - this may take a while)")
            try:
                self.model = whisper.load_model(self.model_size)
                logger.info("Model loaded successfully!")
            except Exception as e:
                logger.log_error_with_exception("Error loading Whisper model", e)
    
    def generate_subtitles(self, video_path, output_format=None, language=None):
        """
        Generate subtitles for a video
        
        Args:
            video_path (str): Path to video file
            output_format (str): Subtitle format (uses config if None)
            language (str): Language code (uses config if None)
        
        Returns:
            str: Path to generated subtitle file
        """
        if not WHISPER_AVAILABLE:
            logger.error("Whisper not available. Install with: pip install openai-whisper")
            return None
        
        if not os.path.exists(video_path):
            logger.error(f"Video file not found: {video_path}")
            return None
        
        output_format = output_format or config.SUBTITLE_FORMAT
        language = language or config.SUBTITLE_LANGUAGE
        
        logger.info(f"Generating subtitles for: {os.path.basename(video_path)}")
        logger.info(f"Language: {language if language != 'auto' else 'Auto-detect'}")
        logger.info(f"Format: {output_format}")
        
        try:
            # Transcribe the video
            transcribe_options = {}
            if language != "auto":
                transcribe_options['language'] = language
            
            result = self.model.transcribe(
                video_path,
                **transcribe_options,
                verbose=False
            )
            
            # Generate subtitle file
            base_path = os.path.splitext(video_path)[0]
            subtitle_path = f"{base_path}.{output_format}"
            
            if output_format == "srt":
                self._write_srt(result, subtitle_path)
            elif output_format == "vtt":
                self._write_vtt(result, subtitle_path)
            elif output_format == "txt":
                self._write_txt(result, subtitle_path)
            else:
                logger.error(f"Unsupported format: {output_format}")
                return None
            
            logger.info(f"Subtitles generated: {subtitle_path}")
            return subtitle_path
            
        except Exception as e:
            logger.log_error_with_exception("Error generating subtitles", e)
            return None
    
    def _write_srt(self, result, output_path):
        """Write subtitles in SRT format"""
        with open(output_path, 'w', encoding='utf-8') as f:
            for i, segment in enumerate(result['segments'], 1):
                start = self._format_timestamp(segment['start'])
                end = self._format_timestamp(segment['end'])
                text = segment['text'].strip()
                
                f.write(f"{i}\n")
                f.write(f"{start} --> {end}\n")
                f.write(f"{text}\n\n")
    
    def _write_vtt(self, result, output_path):
        """Write subtitles in WebVTT format"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("WEBVTT\n\n")
            
            for i, segment in enumerate(result['segments'], 1):
                start = self._format_timestamp(segment['start'])
                end = self._format_timestamp(segment['end'])
                text = segment['text'].strip()
                
                f.write(f"{start} --> {end}\n")
                f.write(f"{text}\n\n")
    
    def _write_txt(self, result, output_path):
        """Write plain text transcript"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result['text'].strip())
    
    def _format_timestamp(self, seconds):
        """Format seconds to SRT timestamp (HH:MM:SS,mmm)"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        
        return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"
    
    def add_subtitles_to_video(self, video_path, subtitle_path, output_path=None,
                               font_size=None, font_color=None, bg_color=None):
        """
        Burn subtitles into video (hardcoded/permanent)
        
        Args:
            video_path (str): Input video path
            subtitle_path (str): Subtitle file path (.srt)
            output_path (str): Output video path (optional)
            font_size (int): Font size (uses config if None)
            font_color (str): Font color (uses config if None)
            bg_color (str): Background color (uses config if None)
        
        Returns:
            str: Path to output video with burned subtitles
        """
        if not os.path.exists(video_path):
            logger.error(f"Video not found: {video_path}")
            return None
        
        if not os.path.exists(subtitle_path):
            logger.error(f"Subtitle file not found: {subtitle_path}")
            return None
        
        # Use config values if not provided
        font_size = font_size or config.SUBTITLE_FONT_SIZE
        font_color = font_color or config.SUBTITLE_FONT_COLOR
        bg_color = bg_color or config.SUBTITLE_BG_COLOR
        
        # Generate output path
        if output_path is None:
            base, ext = os.path.splitext(video_path)
            output_path = f"{base}_with_subtitles{ext}"
        
        logger.info(f"Burning subtitles into video...")
        logger.info(f"Input: {video_path}")
        logger.info(f"Subtitles: {subtitle_path}")
        logger.info(f"Output: {output_path}")
        
        # Escape subtitle path for FFmpeg
        subtitle_path_escaped = subtitle_path.replace('\\', '/').replace(':', '\\:')
        
        try:
            # Build subtitle style string
            style_parts = [
                f"FontSize={font_size}",
                f"PrimaryColour=&H{self._color_to_hex(font_color)}",
                f"BackColour=&H{self._color_to_hex(bg_color)}",
            ]
            
            if config.SUBTITLE_BOLD:
                style_parts.append("Bold=1")
            if config.SUBTITLE_ITALIC:
                style_parts.append("Italic=1")
            if config.SUBTITLE_OUTLINE_WIDTH > 0:
                style_parts.append(f"OutlineColour=&H{self._color_to_hex(config.SUBTITLE_OUTLINE_COLOR)}")
                style_parts.append(f"Outline={config.SUBTITLE_OUTLINE_WIDTH}")
            
            style_string = ','.join(style_parts)
            
            # FFmpeg command to burn subtitles
            cmd = [
                'ffmpeg',
                '-i', video_path,
                '-vf', f"subtitles={subtitle_path_escaped}:force_style='{style_string}'",
                '-c:a', 'copy',  # Copy audio without re-encoding
                '-y',  # Overwrite output
                output_path
            ]
            
            subprocess.run(cmd, check=True, capture_output=True)
            logger.info(f"Video with subtitles created: {output_path}")
            return output_path
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Error adding subtitles: {e}")
            logger.debug(f"Error details: {e.stderr.decode()}")
            return None
        except Exception as e:
            logger.log_error_with_exception("Error burning subtitles", e)
            return None
    
    def _color_to_hex(self, color):
        """Convert color name to hex for FFmpeg"""
        colors = {
            'white': 'FFFFFF',
            'black': '000000',
            'yellow': 'FFFF00',
            'red': 'FF0000',
            'green': '00FF00',
            'blue': '0000FF',
            'cyan': '00FFFF',
            'magenta': 'FF00FF',
        }
        
        # Handle transparency (e.g., "black@0.5")
        if '@' in color:
            color_name, alpha = color.split('@')
            hex_color = colors.get(color_name.lower(), 'FFFFFF')
            alpha_hex = format(int(float(alpha) * 255), '02X')
            return f"{alpha_hex}{hex_color}"
        
        return colors.get(color.lower(), 'FFFFFF')
