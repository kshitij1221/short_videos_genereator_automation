"""
Logging Utility
Provides comprehensive logging for video processing
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
import config


class VideoProcessingLogger:
    """Custom logger for video processing with file and console output"""
    
    def __init__(self, name="VideoProcessor"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, config.LOG_LEVEL))
        
        # Remove existing handlers to avoid duplicates
        self.logger.handlers = []
        
        # Create formatters
        formatter = logging.Formatter(
            config.LOG_FORMAT,
            datefmt=config.LOG_DATE_FORMAT
        )
        
        # Console handler
        if config.LOG_TO_CONSOLE:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(getattr(logging, config.LOG_LEVEL))
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
        
        # File handler with rotation
        if config.LOG_TO_FILE and config.ENABLE_LOGGING:
            log_file_path = os.path.join(config.LOGS_PATH, config.LOG_FILE_NAME)
            
            # Create rotating file handler
            file_handler = RotatingFileHandler(
                log_file_path,
                maxBytes=config.LOG_MAX_SIZE_MB * 1024 * 1024,  # Convert MB to bytes
                backupCount=config.LOG_BACKUP_COUNT
            )
            file_handler.setLevel(getattr(logging, config.LOG_LEVEL))
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def debug(self, message):
        """Log debug message"""
        self.logger.debug(message)
    
    def info(self, message):
        """Log info message"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log warning message"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error message"""
        self.logger.error(message)
    
    def critical(self, message):
        """Log critical message"""
        self.logger.critical(message)
    
    def log_separator(self, char="=", length=70):
        """Log a separator line"""
        self.info(char * length)
    
    def log_section(self, title):
        """Log a section header"""
        self.log_separator()
        self.info(f"  {title}")
        self.log_separator()
    
    def log_config(self):
        """Log current configuration"""
        self.log_section("CONFIGURATION SUMMARY")
        config_summary = config.get_config_summary()
        for key, value in config_summary.items():
            self.info(f"  {key}: {value}")
        self.log_separator()
    
    def log_progress(self, current, total, item_name="Item"):
        """Log progress"""
        percentage = (current / total) * 100 if total > 0 else 0
        self.info(f"Progress: [{current}/{total}] {percentage:.1f}% - Processing {item_name}")
    
    def log_file_created(self, filepath):
        """Log file creation"""
        self.info(f"✅ Created: {filepath}")
    
    def log_file_deleted(self, filepath):
        """Log file deletion"""
        self.info(f"🗑️  Deleted: {filepath}")
    
    def log_error_with_exception(self, message, exception):
        """Log error with exception details"""
        self.error(f"{message}: {str(exception)}")
        self.debug(f"Exception type: {type(exception).__name__}")
    
    def log_processing_start(self, video_name):
        """Log start of video processing"""
        self.log_section(f"PROCESSING: {video_name}")
        self.info(f"Start time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    def log_processing_complete(self, video_name, duration_seconds):
        """Log completion of video processing"""
        self.info(f"End time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.info(f"Duration: {duration_seconds:.2f} seconds ({duration_seconds/60:.2f} minutes)")
        self.log_separator()
        self.info(f"✅ COMPLETED: {video_name}")
        self.log_separator()
    
    def log_subtitle_generation(self, clip_name, language, model):
        """Log subtitle generation"""
        self.info(f"📝 Generating subtitles: {clip_name}")
        self.info(f"   Language: {language} | Model: {model}")
    
    def log_subtitle_complete(self, subtitle_path, duration):
        """Log subtitle generation completion"""
        self.info(f"✅ Subtitles generated in {duration:.2f}s: {subtitle_path}")
    
    def log_video_cut(self, clip_name, start_time, end_time):
        """Log video cutting"""
        self.info(f"✂️  Cutting clip: {clip_name} ({start_time}s - {end_time}s)")
    
    def log_download_start(self, url):
        """Log download start"""
        self.info(f"📥 Downloading from: {url}")
    
    def log_download_complete(self, filepath, size_mb):
        """Log download completion"""
        self.info(f"✅ Download complete: {filepath} ({size_mb:.2f} MB)")
    
    def log_statistics(self, stats_dict):
        """Log processing statistics"""
        self.log_section("PROCESSING STATISTICS")
        for key, value in stats_dict.items():
            self.info(f"  {key}: {value}")
        self.log_separator()


# Create global logger instance
logger = VideoProcessingLogger()


def get_logger():
    """Get the global logger instance"""
    return logger
