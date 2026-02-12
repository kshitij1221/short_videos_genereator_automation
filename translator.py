"""
Subtitle Translator - FREE Translation Module
Translates subtitles from one language to another
Uses deep-translator (100% FREE, no API keys needed!)
"""

import os
import re
from pathlib import Path
import config
from logger import get_logger

logger = get_logger()

try:
    from deep_translator import GoogleTranslator
    TRANSLATOR_AVAILABLE = True
except ImportError:
    TRANSLATOR_AVAILABLE = False
    logger.warning("deep-translator not installed. Translation unavailable.")
    logger.info("Install with: pip install deep-translator")


class SubtitleTranslator:
    """Translate subtitle files between languages"""
    
    def __init__(self):
        """Initialize the translator"""
        if not TRANSLATOR_AVAILABLE:
            logger.error("Translation module not available")
            logger.info("Install with: pip install deep-translator")
        else:
            logger.info("Subtitle translator initialized")
    
    def translate_srt_file(self, srt_path, source_lang, target_lang, output_path=None):
        """
        Translate an SRT subtitle file
        
        Args:
            srt_path (str): Path to source .srt file
            source_lang (str): Source language code ('en', 'hi', etc.)
            target_lang (str): Target language code ('hi', 'en', etc.)
            output_path (str): Output path (optional)
        
        Returns:
            str: Path to translated subtitle file
        """
        if not TRANSLATOR_AVAILABLE:
            logger.error("deep-translator not installed")
            return None
        
        if not os.path.exists(srt_path):
            logger.error(f"Subtitle file not found: {srt_path}")
            return None
        
        logger.info(f"Translating subtitle: {os.path.basename(srt_path)}")
        logger.info(f"From: {source_lang} → To: {target_lang}")
        
        try:
            # Read the SRT file
            with open(srt_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse SRT content
            subtitles = self._parse_srt(content)
            
            # Translate each subtitle
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translated_subtitles = []
            
            total = len(subtitles)
            for idx, subtitle in enumerate(subtitles, 1):
                try:
                    # Translate the text
                    translated_text = translator.translate(subtitle['text'])
                    
                    translated_subtitles.append({
                        'index': subtitle['index'],
                        'timestamp': subtitle['timestamp'],
                        'text': translated_text
                    })
                    
                    if idx % 10 == 0:  # Log progress every 10 subtitles
                        logger.debug(f"Translated {idx}/{total} subtitles")
                    
                except Exception as e:
                    logger.warning(f"Error translating subtitle {idx}: {e}")
                    # Keep original text if translation fails
                    translated_subtitles.append(subtitle)
            
            # Generate output path
            if output_path is None:
                base = os.path.splitext(srt_path)[0]
                output_path = f"{base}_{target_lang}.srt"
            
            # Write translated SRT
            self._write_srt(translated_subtitles, output_path)
            
            logger.info(f"✅ Translation complete: {output_path}")
            return output_path
            
        except Exception as e:
            logger.log_error_with_exception("Error translating subtitle file", e)
            return None
    
    def _parse_srt(self, content):
        """Parse SRT file content"""
        subtitles = []
        blocks = content.strip().split('\n\n')
        
        for block in blocks:
            lines = block.strip().split('\n')
            if len(lines) >= 3:
                index = lines[0].strip()
                timestamp = lines[1].strip()
                text = '\n'.join(lines[2:]).strip()
                
                subtitles.append({
                    'index': index,
                    'timestamp': timestamp,
                    'text': text
                })
        
        return subtitles
    
    def _write_srt(self, subtitles, output_path):
        """Write subtitles to SRT file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            for subtitle in subtitles:
                f.write(f"{subtitle['index']}\n")
                f.write(f"{subtitle['timestamp']}\n")
                f.write(f"{subtitle['text']}\n\n")
    
    def translate_text(self, text, source_lang, target_lang):
        """
        Translate a single text string
        
        Args:
            text (str): Text to translate
            source_lang (str): Source language code
            target_lang (str): Target language code
        
        Returns:
            str: Translated text
        """
        if not TRANSLATOR_AVAILABLE:
            logger.error("deep-translator not installed")
            return text
        
        try:
            translator = GoogleTranslator(source=source_lang, target=target_lang)
            translated = translator.translate(text)
            return translated
        except Exception as e:
            logger.log_error_with_exception("Error translating text", e)
            return text
    
    def batch_translate_subtitles(self, subtitle_folder, source_lang, target_lang):
        """
        Translate all subtitle files in a folder
        
        Args:
            subtitle_folder (str): Folder containing .srt files
            source_lang (str): Source language code
            target_lang (str): Target language code
        
        Returns:
            list: Paths to translated subtitle files
        """
        subtitle_files = list(Path(subtitle_folder).glob("*.srt"))
        
        if not subtitle_files:
            logger.warning(f"No .srt files found in: {subtitle_folder}")
            return []
        
        logger.info(f"Translating {len(subtitle_files)} subtitle files...")
        logger.info(f"From: {source_lang} → To: {target_lang}")
        
        translated_files = []
        
        for idx, srt_path in enumerate(subtitle_files, 1):
            logger.info(f"\n[{idx}/{len(subtitle_files)}] Processing: {srt_path.name}")
            
            translated_path = self.translate_srt_file(
                str(srt_path),
                source_lang,
                target_lang
            )
            
            if translated_path:
                translated_files.append(translated_path)
        
        logger.info(f"\n✅ Batch translation complete: {len(translated_files)}/{len(subtitle_files)}")
        return translated_files
    
    def get_supported_languages(self):
        """Get list of supported language codes"""
        # Common languages supported by Google Translate
        languages = {
            # Indian Languages
            'hi': 'Hindi',
            'bn': 'Bengali',
            'te': 'Telugu',
            'mr': 'Marathi',
            'ta': 'Tamil',
            'ur': 'Urdu',
            'gu': 'Gujarati',
            'kn': 'Kannada',
            'ml': 'Malayalam',
            'pa': 'Punjabi',
            
            # Major World Languages
            'en': 'English',
            'es': 'Spanish',
            'fr': 'French',
            'de': 'German',
            'it': 'Italian',
            'pt': 'Portuguese',
            'ru': 'Russian',
            'ja': 'Japanese',
            'ko': 'Korean',
            'zh-CN': 'Chinese (Simplified)',
            'zh-TW': 'Chinese (Traditional)',
            'ar': 'Arabic',
            'tr': 'Turkish',
            'nl': 'Dutch',
            'pl': 'Polish',
            'vi': 'Vietnamese',
            'th': 'Thai',
            'id': 'Indonesian',
            'ms': 'Malay',
            'fil': 'Filipino',
        }
        return languages
    
    def print_supported_languages(self):
        """Print all supported languages"""
        languages = self.get_supported_languages()
        
        logger.info("=" * 60)
        logger.info("SUPPORTED LANGUAGES FOR TRANSLATION")
        logger.info("=" * 60)
        
        for code, name in sorted(languages.items(), key=lambda x: x[1]):
            logger.info(f"  {code:8s} - {name}")
        
        logger.info("=" * 60)


def translate_subtitle_file(srt_path, target_lang, source_lang='auto'):
    """
    Convenience function to translate a subtitle file
    
    Args:
        srt_path (str): Path to .srt file
        target_lang (str): Target language code
        source_lang (str): Source language code (default: 'auto')
    
    Returns:
        str: Path to translated file
    """
    translator = SubtitleTranslator()
    
    # Auto-detect source language if needed
    if source_lang == 'auto':
        # Try to detect from filename or use English as default
        if '_hi' in srt_path or 'hindi' in srt_path.lower():
            source_lang = 'hi'
        elif '_en' in srt_path or 'english' in srt_path.lower():
            source_lang = 'en'
        else:
            source_lang = 'en'  # Default to English
            logger.info(f"Auto-detected source language: {source_lang}")
    
    return translator.translate_srt_file(srt_path, source_lang, target_lang)


def main():
    """Example usage"""
    logger.log_section("SUBTITLE TRANSLATOR - TEST")
    
    if not TRANSLATOR_AVAILABLE:
        logger.error("deep-translator not installed!")
        logger.info("\n📦 Installation:")
        logger.info("   pip install deep-translator")
        return
    
    translator = SubtitleTranslator()
    
    # Show supported languages
    translator.print_supported_languages()
    
    # Example translation
    print("\n" + "="*60)
    print("Example Translation:")
    print("="*60)
    
    example_text = "Hello, how are you?"
    print(f"\nOriginal (English): {example_text}")
    
    translated = translator.translate_text(example_text, 'en', 'hi')
    print(f"Translated (Hindi): {translated}")
    
    print("\n✅ Translation system ready!")


if __name__ == "__main__":
    main()