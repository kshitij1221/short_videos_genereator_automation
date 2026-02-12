# """
# RUN.PY - Main Video Processing Script
# Everything is controlled by config.py!
# Includes comprehensive logging and organized folder structure.
# """

# import os
# import time
# from pathlib import Path
# from datetime import datetime

# import config
# from logger import get_logger
# from youtube_downloader import YouTubeDownloader
# from video_cutter import VideoCutter
# from subtitle_generator import SubtitleGenerator

# logger = get_logger()


# class VideoProcessor:
#     """Main video processing class with logging and config integration"""
    
#     def __init__(self):
#         self.downloader = None
#         self.subtitle_gen = None
#         self.stats = {
#             "total_clips_created": 0,
#             "clips_with_subtitles": 0,
#             "total_processing_time": 0,
#             "subtitles_generated": 0,
#             "errors": 0
#         }
        
#         logger.log_config()
#         self._initialize_components()
    
#     def _initialize_components(self):
#         """Initialize downloader and subtitle generator"""
#         try:
#             # Initialize YouTube downloader
#             self.downloader = YouTubeDownloader(download_folder=config.DOWNLOAD_PATH)
#             logger.info(" YouTube downloader initialized")
            
#             # Initialize subtitle generator if enabled
#             if config.ENABLE_SUBTITLES:
#                 logger.info(f" Loading Whisper model ({config.WHISPER_MODEL})...")
#                 self.subtitle_gen = SubtitleGenerator(model_size=config.WHISPER_MODEL)
#                 logger.info(" Subtitle generator initialized")
#             else:
#                 logger.info("  Subtitle generation disabled")
                
#         except Exception as e:
#             logger.log_error_with_exception("Error initializing components", e)
#             raise
    
#     def process_video(self, video_source, is_youtube=True):
#         """
#         Main video processing pipeline
        
#         Args:
#             video_source: YouTube URL or local file path
#             is_youtube: True if YouTube URL, False if local file
#         """
#         start_time = time.time()
        
#         try:
#             logger.log_processing_start(video_source)
            
#             # Step 1: Get or download video
#             video_path = self._get_video_path(video_source, is_youtube)
#             if not video_path:
#                 logger.error(" Failed to get video")
#                 self.stats["errors"] += 1
#                 return False
            
#             # Step 2: Cut video into clips
#             clips = self._cut_video(video_path)
#             if not clips:
#                 logger.error(" Failed to create clips")
#                 self.stats["errors"] += 1
#                 return False
            
#             # Step 3: Generate subtitles and burn them
#             if config.ENABLE_SUBTITLES:
#                 self._process_subtitles(clips)
            
#             # Step 4: Cleanup
#             self._cleanup(video_path, is_youtube)
            
#             # Calculate total time
#             total_time = time.time() - start_time
#             self.stats["total_processing_time"] = total_time
            
#             logger.log_processing_complete(video_source, total_time)
#             logger.log_statistics(self.stats)
            
#             return True
            
#         except Exception as e:
#             logger.log_error_with_exception("Error in video processing", e)
#             self.stats["errors"] += 1
#             return False
    
#     def _get_video_path(self, source, is_youtube):
#         """Get video path (download if YouTube, validate if local)"""
#         if is_youtube:
#             logger.log_download_start(source)
            
#             # Get video info first
#             info = self.downloader.get_video_info(source)
#             if info:
#                 logger.info(f"📺 Video: {info['title']}")
#                 logger.info(f"  Duration: {info['duration_formatted']}")
            
#             # Download video
#             video_path = self.downloader.download_video(
#                 source,
#                 quality=config.YOUTUBE_QUALITY
#             )
            
#             if video_path and os.path.exists(video_path):
#                 size_mb = os.path.getsize(video_path) / (1024 * 1024)
#                 logger.log_download_complete(video_path, size_mb)
#                 return video_path
#             else:
#                 logger.error(" Download failed")
#                 return None
#         else:
#             # Local file
#             if os.path.exists(source):
#                 logger.info(f"📹 Using local video: {source}")
#                 size_mb = os.path.getsize(source) / (1024 * 1024)
#                 logger.info(f"   Size: {size_mb:.2f} MB")
#                 return source
#             else:
#                 logger.error(f" Local video not found: {source}")
#                 return None
    
#     def _cut_video(self, video_path):
#         """Cut video into clips"""
#         logger.log_section("CUTTING VIDEO INTO CLIPS")
#         logger.info(f" Output folder: {config.CLIPS_PATH}")
#         logger.info(f"  Clip duration: {config.CLIP_DURATION} seconds")
        
#         try:
#             cutter = VideoCutter(
#                 input_video=video_path,
#                 output_folder=config.CLIPS_PATH,
#                 clip_duration=config.CLIP_DURATION
#             )
            
#             # Get video duration
#             duration = cutter.get_video_duration()
#             if duration:
#                 estimated_clips = int(duration // config.CLIP_DURATION)
#                 logger.info(f" Estimated clips: {estimated_clips}")
            
#             # Cut video
#             cutter.cut_video_segments()
            
#             # Get created clips
#             clips = sorted(Path(config.CLIPS_PATH).glob("*.mp4"))
#             self.stats["total_clips_created"] = len(clips)
#             logger.info(f" Created {len(clips)} clips")
            
#             return clips
            
#         except Exception as e:
#             logger.log_error_with_exception("Error cutting video", e)
#             return []
    
#     def _process_subtitles(self, clips):
#         """Generate and burn subtitles for all clips"""
#         if not clips:
#             logger.warning("  No clips to process")
#             return
        
#         logger.log_section("GENERATING SUBTITLES")
#         logger.info(f" Format: {config.SUBTITLE_FORMAT}")
#         logger.info(f" Language: {config.SUBTITLE_LANGUAGE}")
#         logger.info(f" Model: {config.WHISPER_MODEL}")
#         logger.info(f" Burn into video: {config.BURN_SUBTITLES}")
        
#         for idx, clip_path in enumerate(clips, 1):
#             try:
#                 logger.log_progress(idx, len(clips), clip_path.name)
                
#                 # Check if already processed
#                 if config.SKIP_EXISTING_SUBTITLES:
#                     subtitle_path = str(clip_path).replace('.mp4', f'.{config.SUBTITLE_FORMAT}')
#                     if os.path.exists(subtitle_path):
#                         logger.info(f"  Skipping (subtitle exists): {clip_path.name}")
#                         continue
                
#                 # Generate subtitles
#                 subtitle_start = time.time()
#                 logger.log_subtitle_generation(
#                     clip_path.name,
#                     config.SUBTITLE_LANGUAGE,
#                     config.WHISPER_MODEL
#                 )
                
#                 subtitle_path = self.subtitle_gen.generate_subtitles(
#                     str(clip_path),
#                     output_format=config.SUBTITLE_FORMAT,
#                     language=config.SUBTITLE_LANGUAGE
#                 )
                
#                 subtitle_duration = time.time() - subtitle_start
                
#                 if subtitle_path:
#                     self.stats["subtitles_generated"] += 1
#                     logger.log_subtitle_complete(subtitle_path, subtitle_duration)
                    
#                     # Move subtitle to subtitle files folder
#                     subtitle_filename = os.path.basename(subtitle_path)
#                     new_subtitle_path = os.path.join(
#                         config.SUBTITLE_FILES_PATH,
#                         subtitle_filename
#                     )
#                     os.rename(subtitle_path, new_subtitle_path)
#                     logger.info(f" Moved subtitle to: {config.SUBTITLE_FILES_PATH}/")
                    
#                     # Burn subtitles into video if enabled
#                     if config.BURN_SUBTITLES:
#                         self._burn_subtitles(clip_path, new_subtitle_path)
                    
#                 else:
#                     logger.error(f" Failed to generate subtitles for: {clip_path.name}")
#                     self.stats["errors"] += 1
                    
#             except Exception as e:
#                 logger.log_error_with_exception(f"Error processing {clip_path.name}", e)
#                 self.stats["errors"] += 1
        
#         logger.info(f" Subtitle generation complete: {self.stats['subtitles_generated']}/{len(clips)}")
    
#     def _burn_subtitles(self, clip_path, subtitle_path):
#         """Burn subtitles into video"""
#         try:
#             output_filename = clip_path.stem + "_subtitled" + clip_path.suffix
#             output_path = os.path.join(config.CLIPS_WITH_SUBTITLES_PATH, output_filename)
            
#             logger.info(f" Burning subtitles into: {clip_path.name}")
            
#             result = self.subtitle_gen.add_subtitles_to_video(
#                 str(clip_path),
#                 subtitle_path,
#                 output_path,
#                 font_size=config.SUBTITLE_FONT_SIZE,
#                 font_color=config.SUBTITLE_FONT_COLOR,
#                 bg_color=config.SUBTITLE_BG_COLOR
#             )
            
#             if result:
#                 self.stats["clips_with_subtitles"] += 1
#                 logger.log_file_created(output_path)
                
#                 # Delete original clip if configured
#                 if config.DELETE_ORIGINAL_CLIPS:
#                     os.remove(clip_path)
#                     logger.log_file_deleted(str(clip_path))
#             else:
#                 logger.error(f" Failed to burn subtitles for: {clip_path.name}")
#                 self.stats["errors"] += 1
                
#         except Exception as e:
#             logger.log_error_with_exception(f"Error burning subtitles", e)
#             self.stats["errors"] += 1
    
#     def _cleanup(self, video_path, is_youtube):
#         """Cleanup temporary files"""
#         if is_youtube and config.DELETE_DOWNLOADED_VIDEO:
#             try:
#                 if os.path.exists(video_path):
#                     os.remove(video_path)
#                     logger.log_file_deleted(video_path)
#             except Exception as e:
#                 logger.log_error_with_exception("Error deleting downloaded video", e)


# def main():
#     """Main entry point"""
#     logger.log_section("VIDEO PROCESSING STARTED")
#     logger.info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
#     try:
#         processor = VideoProcessor()
        
#         # Determine video source
#         if config.YOUTUBE_URL:
#             logger.info("📺 Mode: YouTube URL")
#             success = processor.process_video(config.YOUTUBE_URL, is_youtube=True)
#         elif config.LOCAL_VIDEO_PATH:
#             logger.info(" Mode: Local file")
#             success = processor.process_video(config.LOCAL_VIDEO_PATH, is_youtube=False)
#         else:
#             logger.error(" No video source specified in config.py!")
#             logger.info("Please set either YOUTUBE_URL or LOCAL_VIDEO_PATH")
#             return
        
#         if success:
#             logger.log_section(" ALL PROCESSING COMPLETE!")
#             logger.info(f" Clips folder: {config.CLIPS_PATH}")
#             if config.ENABLE_SUBTITLES and config.BURN_SUBTITLES:
#                 logger.info(f" Clips with subtitles: {config.CLIPS_WITH_SUBTITLES_PATH}")
#             if config.ENABLE_SUBTITLES:
#                 logger.info(f" Subtitle files: {config.SUBTITLE_FILES_PATH}")
#             logger.info(f"📋 Log file: {os.path.join(config.LOGS_PATH, config.LOG_FILE_NAME)}")
#         else:
#             logger.error(" Processing failed - check logs for details")
            
#     except KeyboardInterrupt:
#         logger.warning("\n⏸️  Processing interrupted by user (Ctrl+C)")
#     except Exception as e:
#         logger.log_error_with_exception("Fatal error in main", e)
#         raise


# if __name__ == "__main__":
#     main()


"""
RUN.PY - Main Video Processing Script
Everything is controlled by config.py!
Includes comprehensive logging and organized folder structure.
"""

import os
import time
from pathlib import Path
from datetime import datetime

import config
from logger import get_logger
from youtube_downloader import YouTubeDownloader
from video_cutter import VideoCutter
from subtitle_generator import SubtitleGenerator
from translator import SubtitleTranslator

logger = get_logger()


class VideoProcessor:
    """Main video processing class with logging and config integration"""
    
    def __init__(self):
        self.downloader = None
        self.subtitle_gen = None
        self.translator = None
        self.stats = {
            "total_clips_created": 0,
            "clips_with_subtitles": 0,
            "clips_translated": 0,
            "total_processing_time": 0,
            "subtitles_generated": 0,
            "errors": 0
        }
        
        logger.log_config()
        self._initialize_components()
    
    def _initialize_components(self):
        """Initialize downloader and subtitle generator"""
        try:
            # Initialize YouTube downloader
            self.downloader = YouTubeDownloader(download_folder=config.DOWNLOAD_PATH)
            logger.info(" YouTube downloader initialized")
            
            # Initialize subtitle generator if enabled
            if config.ENABLE_SUBTITLES:
                logger.info(f" Loading Whisper model ({config.WHISPER_MODEL})...")
                self.subtitle_gen = SubtitleGenerator(model_size=config.WHISPER_MODEL)
                logger.info(" Subtitle generator initialized")
            else:
                logger.info("  Subtitle generation disabled")
            
            # Initialize translator if enabled
            if config.ENABLE_TRANSLATION:
                logger.info(" Initializing translator...")
                self.translator = SubtitleTranslator()
                logger.info(f" Translator initialized (Target: {config.TRANSLATION_TARGET_LANG})")
            else:
                logger.info("  Translation disabled")
                
        except Exception as e:
            logger.log_error_with_exception("Error initializing components", e)
            raise
    
    def process_video(self, video_source, is_youtube=True):
        """
        Main video processing pipeline
        
        Args:
            video_source: YouTube URL or local file path
            is_youtube: True if YouTube URL, False if local file
        """
        start_time = time.time()
        
        try:
            logger.log_processing_start(video_source)
            
            # Step 1: Get or download video
            video_path = self._get_video_path(video_source, is_youtube)
            if not video_path:
                logger.error(" Failed to get video")
                self.stats["errors"] += 1
                return False
            
            # Step 2: Cut video into clips
            clips = self._cut_video(video_path)
            if not clips:
                logger.error(" Failed to create clips")
                self.stats["errors"] += 1
                return False
            
            # Step 3: Generate subtitles and burn them
            if config.ENABLE_SUBTITLES:
                self._process_subtitles(clips)
            
            # Step 4: Translate subtitles if enabled
            if config.ENABLE_TRANSLATION and config.ENABLE_SUBTITLES:
                self._translate_subtitles()
            
            # Step 5: Cleanup
            self._cleanup(video_path, is_youtube)
            
            # Calculate total time
            total_time = time.time() - start_time
            self.stats["total_processing_time"] = total_time
            
            logger.log_processing_complete(video_source, total_time)
            logger.log_statistics(self.stats)
            
            return True
            
        except Exception as e:
            logger.log_error_with_exception("Error in video processing", e)
            self.stats["errors"] += 1
            return False
    
    def _get_video_path(self, source, is_youtube):
        """Get video path (download if YouTube, validate if local)"""
        if is_youtube:
            logger.log_download_start(source)
            
            # Get video info first
            info = self.downloader.get_video_info(source)
            if info:
                logger.info(f" Video: {info['title']}")
                logger.info(f"  Duration: {info['duration_formatted']}")
            
            # Download video
            video_path = self.downloader.download_video(
                source,
                quality=config.YOUTUBE_QUALITY
            )
            
            if video_path and os.path.exists(video_path):
                size_mb = os.path.getsize(video_path) / (1024 * 1024)
                logger.log_download_complete(video_path, size_mb)
                return video_path
            else:
                logger.error(" Download failed")
                return None
        else:
            # Local file
            if os.path.exists(source):
                logger.info(f"📹 Using local video: {source}")
                size_mb = os.path.getsize(source) / (1024 * 1024)
                logger.info(f"   Size: {size_mb:.2f} MB")
                return source
            else:
                logger.error(f" Local video not found: {source}")
                return None
    
    def _cut_video(self, video_path):
        """Cut video into clips"""
        logger.log_section("CUTTING VIDEO INTO CLIPS")
        logger.info(f" Output folder: {config.CLIPS_PATH}")
        logger.info(f"  Clip duration: {config.CLIP_DURATION} seconds")
        
        try:
            cutter = VideoCutter(
                input_video=video_path,
                output_folder=config.CLIPS_PATH,
                clip_duration=config.CLIP_DURATION
            )
            
            # Get video duration
            duration = cutter.get_video_duration()
            if duration:
                estimated_clips = int(duration // config.CLIP_DURATION)
                logger.info(f" Estimated clips: {estimated_clips}")
            
            # Cut video
            cutter.cut_video_segments()
            
            # Get created clips
            clips = sorted(Path(config.CLIPS_PATH).glob("*.mp4"))
            self.stats["total_clips_created"] = len(clips)
            logger.info(f" Created {len(clips)} clips")
            
            return clips
            
        except Exception as e:
            logger.log_error_with_exception("Error cutting video", e)
            return []
    
    def _process_subtitles(self, clips):
        """Generate and burn subtitles for all clips"""
        if not clips:
            logger.warning("  No clips to process")
            return
        
        logger.log_section("GENERATING SUBTITLES")
        logger.info(f" Format: {config.SUBTITLE_FORMAT}")
        logger.info(f" Language: {config.SUBTITLE_LANGUAGE}")
        logger.info(f" Model: {config.WHISPER_MODEL}")
        logger.info(f" Burn into video: {config.BURN_SUBTITLES}")
        
        for idx, clip_path in enumerate(clips, 1):
            try:
                logger.log_progress(idx, len(clips), clip_path.name)
                
                # Check if already processed
                if config.SKIP_EXISTING_SUBTITLES:
                    subtitle_path = str(clip_path).replace('.mp4', f'.{config.SUBTITLE_FORMAT}')
                    if os.path.exists(subtitle_path):
                        logger.info(f"  Skipping (subtitle exists): {clip_path.name}")
                        continue
                
                # Generate subtitles
                subtitle_start = time.time()
                logger.log_subtitle_generation(
                    clip_path.name,
                    config.SUBTITLE_LANGUAGE,
                    config.WHISPER_MODEL
                )
                
                subtitle_path = self.subtitle_gen.generate_subtitles(
                    str(clip_path),
                    output_format=config.SUBTITLE_FORMAT,
                    language=config.SUBTITLE_LANGUAGE
                )
                
                subtitle_duration = time.time() - subtitle_start
                
                if subtitle_path:
                    self.stats["subtitles_generated"] += 1
                    logger.log_subtitle_complete(subtitle_path, subtitle_duration)
                    
                    # Move subtitle to subtitle files folder
                    subtitle_filename = os.path.basename(subtitle_path)
                    new_subtitle_path = os.path.join(
                        config.SUBTITLE_FILES_PATH,
                        subtitle_filename
                    )
                    os.rename(subtitle_path, new_subtitle_path)
                    logger.info(f" Moved subtitle to: {config.SUBTITLE_FILES_PATH}/")
                    
                    # Burn subtitles into video if enabled
                    if config.BURN_SUBTITLES:
                        self._burn_subtitles(clip_path, new_subtitle_path)
                    
                else:
                    logger.error(f" Failed to generate subtitles for: {clip_path.name}")
                    self.stats["errors"] += 1
                    
            except Exception as e:
                logger.log_error_with_exception(f"Error processing {clip_path.name}", e)
                self.stats["errors"] += 1
        
        logger.info(f" Subtitle generation complete: {self.stats['subtitles_generated']}/{len(clips)}")
    
    def _burn_subtitles(self, clip_path, subtitle_path):
        """Burn subtitles into video"""
        try:
            output_filename = clip_path.stem + "_subtitled" + clip_path.suffix
            output_path = os.path.join(config.CLIPS_WITH_SUBTITLES_PATH, output_filename)
            
            logger.info(f" Burning subtitles into: {clip_path.name}")
            
            result = self.subtitle_gen.add_subtitles_to_video(
                str(clip_path),
                subtitle_path,
                output_path,
                font_size=config.SUBTITLE_FONT_SIZE,
                font_color=config.SUBTITLE_FONT_COLOR,
                bg_color=config.SUBTITLE_BG_COLOR
            )
            
            if result:
                self.stats["clips_with_subtitles"] += 1
                logger.log_file_created(output_path)
                
                # Delete original clip if configured
                if config.DELETE_ORIGINAL_CLIPS:
                    os.remove(clip_path)
                    logger.log_file_deleted(str(clip_path))
            else:
                logger.error(f" Failed to burn subtitles for: {clip_path.name}")
                self.stats["errors"] += 1
                
        except Exception as e:
            logger.log_error_with_exception(f"Error burning subtitles", e)
            self.stats["errors"] += 1
    
    def _translate_subtitles(self):
        """Translate all subtitle files"""
        logger.log_section("TRANSLATING SUBTITLES")
        
        # Get all subtitle files
        subtitle_files = list(Path(config.SUBTITLE_FILES_PATH).glob("*.srt"))
        
        if not subtitle_files:
            logger.warning("No subtitle files found to translate")
            return
        
        # Determine source language
        source_lang = config.TRANSLATION_SOURCE_LANG
        if source_lang == "auto":
            source_lang = config.SUBTITLE_LANGUAGE
            if source_lang == "auto":
                source_lang = "en"  # Default to English
                logger.info(f"Auto-detected source language: {source_lang}")
        
        logger.info(f"Translating {len(subtitle_files)} subtitle files")
        logger.info(f"From: {source_lang} → To: {config.TRANSLATION_TARGET_LANG}")
        
        # Create translated folder
        translated_folder = config.CLIPS_WITH_SUBTITLES_PATH + config.TRANSLATION_FOLDER_SUFFIX
        Path(translated_folder).mkdir(parents=True, exist_ok=True)
        
        for idx, srt_path in enumerate(subtitle_files, 1):
            try:
                logger.log_progress(idx, len(subtitle_files), srt_path.name)
                
                # Translate subtitle file
                translated_srt = self.translator.translate_srt_file(
                    str(srt_path),
                    source_lang,
                    config.TRANSLATION_TARGET_LANG
                )
                
                if translated_srt:
                    self.stats["clips_translated"] += 1
                    
                    # Move translated subtitle to subtitle files folder
                    translated_filename = f"{srt_path.stem}_{config.TRANSLATION_TARGET_LANG}.srt"
                    new_translated_path = os.path.join(
                        config.SUBTITLE_FILES_PATH,
                        translated_filename
                    )
                    
                    # Rename the translated file
                    if os.path.exists(translated_srt):
                        os.rename(translated_srt, new_translated_path)
                        logger.info(f" Saved translated subtitle: {translated_filename}")
                    
                    # Burn translated subtitles into video if enabled
                    if config.BURN_SUBTITLES:
                        # Find corresponding video clip
                        clip_name = srt_path.stem + ".mp4"
                        clip_path = os.path.join(config.CLIPS_PATH, clip_name)
                        
                        if os.path.exists(clip_path):
                            output_filename = f"{srt_path.stem}_{config.TRANSLATION_TARGET_LANG}_subtitled.mp4"
                            output_path = os.path.join(translated_folder, output_filename)
                            
                            logger.info(f" Burning translated subtitles: {output_filename}")
                            
                            result = self.subtitle_gen.add_subtitles_to_video(
                                clip_path,
                                new_translated_path,
                                output_path,
                                font_size=config.SUBTITLE_FONT_SIZE,
                                font_color=config.SUBTITLE_FONT_COLOR,
                                bg_color=config.SUBTITLE_BG_COLOR
                            )
                            
                            if result:
                                logger.log_file_created(output_path)
                        else:
                            logger.warning(f"Video clip not found: {clip_name}")
                else:
                    logger.error(f"Failed to translate: {srt_path.name}")
                    self.stats["errors"] += 1
                    
            except Exception as e:
                logger.log_error_with_exception(f"Error translating {srt_path.name}", e)
                self.stats["errors"] += 1
        
        logger.info(f" Translation complete: {self.stats['clips_translated']}/{len(subtitle_files)}")
        logger.info(f" Translated clips saved in: {translated_folder}")
    
    def _cleanup(self, video_path, is_youtube):
        """Cleanup temporary files"""
        if is_youtube and config.DELETE_DOWNLOADED_VIDEO:
            try:
                if os.path.exists(video_path):
                    os.remove(video_path)
                    logger.log_file_deleted(video_path)
            except Exception as e:
                logger.log_error_with_exception("Error deleting downloaded video", e)


def main():
    """Main entry point"""
    logger.log_section("VIDEO PROCESSING STARTED")
    logger.info(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        processor = VideoProcessor()
        
        # Determine video source
        if config.YOUTUBE_URL:
            logger.info(" Mode: YouTube URL")
            success = processor.process_video(config.YOUTUBE_URL, is_youtube=True)
        elif config.LOCAL_VIDEO_PATH:
            logger.info(" Mode: Local file")
            success = processor.process_video(config.LOCAL_VIDEO_PATH, is_youtube=False)
        else:
            logger.error(" No video source specified in config.py!")
            logger.info("Please set either YOUTUBE_URL or LOCAL_VIDEO_PATH")
            return
        
        if success:
            logger.log_section(" ALL PROCESSING COMPLETE!")
            logger.info(f" Clips folder: {config.CLIPS_PATH}")
            if config.ENABLE_SUBTITLES and config.BURN_SUBTITLES:
                logger.info(f" Clips with subtitles: {config.CLIPS_WITH_SUBTITLES_PATH}")
            if config.ENABLE_SUBTITLES:
                logger.info(f" Subtitle files: {config.SUBTITLE_FILES_PATH}")
            logger.info(f" Log file: {os.path.join(config.LOGS_PATH, config.LOG_FILE_NAME)}")
        else:
            logger.error(" Processing failed - check logs for details")
            
    except KeyboardInterrupt:
        logger.warning("\n⏸  Processing interrupted by user (Ctrl+C)")
    except Exception as e:
        logger.log_error_with_exception("Fatal error in main", e)
        raise


if __name__ == "__main__":
    main()
