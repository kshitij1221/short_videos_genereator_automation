# """
# COMPLETE CONFIGURATION FILE
# All settings in one place - modify as needed!
# """

# import os
# from pathlib import Path

# # ============================================================================
# # VIDEO SOURCE SETTINGS
# # ============================================================================

# # YouTube URL (leave empty if using local file)
# YOUTUBE_URL = "https://youtu.be/pT-Xz9PZulU?si=x2BL87X1nfM9bX4t"

# # OR Local video file path (leave empty if using YouTube)
# LOCAL_VIDEO_PATH = ""

# # YouTube download quality
# # Options: 'best', '2160p', '1080p', '720p', '480p', '360p', 'worst'
# YOUTUBE_QUALITY = '720p'

# # ============================================================================
# # OUTPUT FOLDER STRUCTURE
# # ============================================================================

# # Main output directory
# OUTPUT_BASE_DIR = "output"

# # Subfolder names (will be created under OUTPUT_BASE_DIR)
# DOWNLOADS_FOLDER = "downloads"          # YouTube downloads go here
# CLIPS_FOLDER = "clips"                  # Video clips without subtitles
# CLIPS_WITH_SUBTITLES_FOLDER = "clips_with_subtitles"  # Final clips with subtitles
# SUBTITLE_FILES_FOLDER = "subtitle_files"  # Separate .srt files
# LOGS_FOLDER = "logs"                    # Log files

# # Auto-create full paths (don't modify these)
# DOWNLOAD_PATH = os.path.join(OUTPUT_BASE_DIR, DOWNLOADS_FOLDER)
# CLIPS_PATH = os.path.join(OUTPUT_BASE_DIR, CLIPS_FOLDER)
# CLIPS_WITH_SUBTITLES_PATH = os.path.join(OUTPUT_BASE_DIR, CLIPS_WITH_SUBTITLES_FOLDER)
# SUBTITLE_FILES_PATH = os.path.join(OUTPUT_BASE_DIR, SUBTITLE_FILES_FOLDER)
# LOGS_PATH = os.path.join(OUTPUT_BASE_DIR, LOGS_FOLDER)

# # ============================================================================
# # VIDEO CUTTING SETTINGS
# # ============================================================================

# # Clip duration in seconds
# CLIP_DURATION = 20

# # Video encoding quality
# VIDEO_CODEC = "libx264"
# VIDEO_BITRATE = "2000k"  # Higher = better quality, larger files

# # Audio encoding quality
# AUDIO_CODEC = "aac"
# AUDIO_BITRATE = "192k"

# # Encoding speed preset
# # Options: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
# # ultrafast = fastest encoding, larger files
# # veryslow = slowest encoding, best compression
# ENCODING_PRESET = "medium"

# # ============================================================================
# # SUBTITLE SETTINGS
# # ============================================================================

# # Enable/disable subtitle generation
# ENABLE_SUBTITLES = True

# # Subtitle format
# # Options: 'srt' (most compatible), 'vtt' (web), 'txt' (plain text)
# SUBTITLE_FORMAT = "srt"

# # Language detection
# # Options: 'auto' (auto-detect), 'en', 'es', 'fr', 'de', 'hi', 'zh', 'ja', 'ko', 'ar', 'pt', 'ru', etc.
# SUBTITLE_LANGUAGE = "hi"

# # Whisper AI model size
# # Options: 'tiny', 'base', 'small', 'medium', 'large'
# # tiny:   Fastest, least accurate (~1GB RAM, ~32x realtime)
# # base:   Fast, good accuracy (~1GB RAM, ~16x realtime) ⭐ RECOMMENDED
# # small:  Slower, better accuracy (~2GB RAM, ~6x realtime)
# # medium: Slow, great accuracy (~5GB RAM, ~2x realtime)
# # large:  Slowest, best accuracy (~10GB RAM, ~1x realtime)
# WHISPER_MODEL = "base"

# # Burn subtitles into video?
# # True = Hardcode subtitles permanently into video (recommended for social media)
# # False = Keep subtitles as separate .srt files
# BURN_SUBTITLES = True

# # ============================================================================
# # SUBTITLE STYLING (Applied when BURN_SUBTITLES = True)
# # ============================================================================

# # Font size (recommended: 20-36)
# # 20-24: Small, for desktop viewing
# # 24-28: Medium, good for mobile ⭐ RECOMMENDED
# # 28-36: Large, best for TikTok/Reels
# SUBTITLE_FONT_SIZE = 28

# # Font name (system fonts)
# # Common options: 'Arial', 'Helvetica', 'Verdana', 'Impact', 'Comic Sans MS'
# # Leave as default for cross-platform compatibility
# SUBTITLE_FONT_NAME = "Arial"

# # Font color
# # Options: 'white', 'yellow', 'black', 'red', 'green', 'blue', 'cyan', 'magenta'
# # yellow = High visibility, great for social media ⭐ RECOMMENDED
# # white = Clean, professional
# SUBTITLE_FONT_COLOR = "yellow"

# # Font outline/border color
# # Options: 'black', 'white', 'none'
# # Helps text stand out against any background
# SUBTITLE_OUTLINE_COLOR = "black"

# # Outline width (0-4)
# # 0 = no outline
# # 2 = medium outline ⭐ RECOMMENDED
# # 4 = thick outline
# SUBTITLE_OUTLINE_WIDTH = 2

# # Background box behind text
# # Format: "color@transparency"
# # Examples:
# #   "black@0.0"  = No background (transparent)
# #   "black@0.5"  = 50% transparent black
# #   "black@0.7"  = 70% transparent black ⭐ RECOMMENDED
# #   "black@1.0"  = Solid black box
# SUBTITLE_BG_COLOR = "black@0.7"

# # Subtitle position
# # Options: 'bottom', 'top', 'center'
# SUBTITLE_POSITION = "bottom"

# # Vertical margin from edge (in pixels)
# # Higher number = more space from edge
# SUBTITLE_MARGIN_V = 20

# # Bold text
# SUBTITLE_BOLD = True

# # Italic text
# SUBTITLE_ITALIC = False

# # ============================================================================
# # LOGGING SETTINGS
# # ============================================================================

# # Enable detailed logging
# ENABLE_LOGGING = True

# # Log level
# # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
# # DEBUG = Everything (most detailed)
# # INFO = General information ⭐ RECOMMENDED
# # WARNING = Only warnings and errors
# # ERROR = Only errors
# LOG_LEVEL = "INFO"

# # Log to console (print to screen)
# LOG_TO_CONSOLE = True

# # Log to file
# LOG_TO_FILE = True

# # Log file name (will be in LOGS_FOLDER)
# LOG_FILE_NAME = "video_processing.log"

# # Maximum log file size (in MB) before rotation
# LOG_MAX_SIZE_MB = 10

# # Number of backup log files to keep
# LOG_BACKUP_COUNT = 5

# # Log format
# # Don't modify unless you know what you're doing
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# # ============================================================================
# # PROCESSING OPTIONS
# # ============================================================================

# # Delete original clips after adding subtitles?
# # True = Keep only clips with subtitles (saves space)
# # False = Keep both versions
# DELETE_ORIGINAL_CLIPS = False

# # Delete downloaded YouTube video after processing?
# # True = Save space
# # False = Keep original download
# DELETE_DOWNLOADED_VIDEO = False

# # Maximum concurrent subtitle generation processes
# # Higher = faster but uses more RAM
# # 1 = Process one at a time (safest) ⭐ RECOMMENDED
# # 2-4 = Faster if you have good CPU/RAM
# MAX_CONCURRENT_PROCESSES = 1

# # Skip clips that already have subtitles
# SKIP_EXISTING_SUBTITLES = True

# # ============================================================================
# # BATCH PROCESSING (Multiple videos)
# # ============================================================================

# # List of YouTube URLs to process (leave empty if not batch processing)
# BATCH_YOUTUBE_URLS = [
#     # "https://youtu.be/VIDEO_ID_1",
#     # "https://youtu.be/VIDEO_ID_2",
#     # "https://youtu.be/VIDEO_ID_3",
# ]

# # List of local video files to process
# BATCH_LOCAL_FILES = [
#     # "video1.mp4",
#     # "video2.mp4",
#     # "video3.mp4",
# ]

# # ============================================================================
# # ADVANCED SETTINGS (Rarely need to change)
# # ============================================================================

# # Create separate output folder for each video?
# # True = Each video gets its own subfolder
# # False = All clips in same folder
# SEPARATE_FOLDERS_PER_VIDEO = False

# # Clip naming format
# # Available variables: {index}, {start}, {end}, {duration}
# CLIP_NAME_FORMAT = "clip_{index:03d}_{start}s_to_{end}s"

# # Include timestamp in folder names?
# INCLUDE_TIMESTAMP_IN_FOLDERS = False

# # Temporary files directory
# TEMP_FOLDER = "temp"

# # Clean up temporary files after processing?
# CLEANUP_TEMP_FILES = True

# # ============================================================================
# # SOCIAL MEDIA PRESETS (Quick configurations)
# # ============================================================================

# # Uncomment one of these to quickly configure for specific platforms:

# # # TikTok Preset
# # CLIP_DURATION = 20
# # SUBTITLE_FONT_SIZE = 32
# # SUBTITLE_FONT_COLOR = "yellow"
# # SUBTITLE_BG_COLOR = "black@0.7"
# # SUBTITLE_POSITION = "bottom"
# # BURN_SUBTITLES = True

# # # Instagram Reels Preset
# CLIP_DURATION = 20
# SUBTITLE_FONT_SIZE = 28
# SUBTITLE_FONT_COLOR = "white"
# SUBTITLE_BG_COLOR = "black@0.6"
# SUBTITLE_POSITION = "bottom"
# BURN_SUBTITLES = True

# # # YouTube Shorts Preset
# # CLIP_DURATION = 30
# # SUBTITLE_FONT_SIZE = 30
# # SUBTITLE_FONT_COLOR = "yellow"
# # SUBTITLE_BG_COLOR = "black@0.7"
# # SUBTITLE_POSITION = "bottom"
# # BURN_SUBTITLES = True

# # ============================================================================
# # HELPER FUNCTIONS
# # ============================================================================

# def time_to_seconds(hours=0, minutes=0, seconds=0):
#     """
#     Convert time to seconds
    
#     Examples:
#         time_to_seconds(minutes=5, seconds=30)  # Returns 330
#         time_to_seconds(hours=1, minutes=15)     # Returns 4500
#     """
#     return hours * 3600 + minutes * 60 + seconds


# def create_all_directories():
#     """Create all necessary directories"""
#     directories = [
#         OUTPUT_BASE_DIR,
#         DOWNLOAD_PATH,
#         CLIPS_PATH,
#         CLIPS_WITH_SUBTITLES_PATH,
#         SUBTITLE_FILES_PATH,
#         LOGS_PATH,
#     ]
    
#     if CLEANUP_TEMP_FILES:
#         directories.append(TEMP_FOLDER)
    
#     for directory in directories:
#         Path(directory).mkdir(parents=True, exist_ok=True)


# def get_config_summary():
#     """Get a summary of current configuration"""
#     summary = {
#         "Video Source": YOUTUBE_URL if YOUTUBE_URL else LOCAL_VIDEO_PATH,
#         "Clip Duration": f"{CLIP_DURATION} seconds",
#         "Subtitles Enabled": ENABLE_SUBTITLES,
#         "Burn Subtitles": BURN_SUBTITLES if ENABLE_SUBTITLES else "N/A",
#         "Subtitle Language": SUBTITLE_LANGUAGE if ENABLE_SUBTITLES else "N/A",
#         "Whisper Model": WHISPER_MODEL if ENABLE_SUBTITLES else "N/A",
#         "Font Size": SUBTITLE_FONT_SIZE if ENABLE_SUBTITLES else "N/A",
#         "Font Color": SUBTITLE_FONT_COLOR if ENABLE_SUBTITLES else "N/A",
#         "Output Directory": OUTPUT_BASE_DIR,
#         "Logging Enabled": ENABLE_LOGGING,
#     }
#     return summary


# # Auto-create directories when config is imported
# create_all_directories()


"""
COMPLETE CONFIGURATION FILE
All settings in one place - modify as needed!
"""

import os
from pathlib import Path

# ============================================================================
# VIDEO SOURCE SETTINGS
# ============================================================================

# YouTube URL (leave empty if using local file)
YOUTUBE_URL = "https://youtu.be/DGU0wXMKqf4?si=bLn_F-DnIqQqZ2NJ"

# OR Local video file path (leave empty if using YouTube)
LOCAL_VIDEO_PATH = ""

# YouTube download quality
# Options: 'best', '2160p', '1080p', '720p', '480p', '360p', 'worst'
YOUTUBE_QUALITY = '720p'

# ============================================================================
# OUTPUT FOLDER STRUCTURE
# ============================================================================

# Main output directory
OUTPUT_BASE_DIR = "output"

# Subfolder names (will be created under OUTPUT_BASE_DIR)
DOWNLOADS_FOLDER = "downloads"          # YouTube downloads go here
CLIPS_FOLDER = "clips"                  # Video clips without subtitles
CLIPS_WITH_SUBTITLES_FOLDER = "clips_with_subtitles"  # Final clips with subtitles
SUBTITLE_FILES_FOLDER = "subtitle_files"  # Separate .srt files
LOGS_FOLDER = "logs"                    # Log files

# Auto-create full paths (don't modify these)
DOWNLOAD_PATH = os.path.join(OUTPUT_BASE_DIR, DOWNLOADS_FOLDER)
CLIPS_PATH = os.path.join(OUTPUT_BASE_DIR, CLIPS_FOLDER)
CLIPS_WITH_SUBTITLES_PATH = os.path.join(OUTPUT_BASE_DIR, CLIPS_WITH_SUBTITLES_FOLDER)
SUBTITLE_FILES_PATH = os.path.join(OUTPUT_BASE_DIR, SUBTITLE_FILES_FOLDER)
LOGS_PATH = os.path.join(OUTPUT_BASE_DIR, LOGS_FOLDER)

# ============================================================================
# VIDEO CUTTING SETTINGS
# ============================================================================

# Clip duration in seconds
CLIP_DURATION = 20

# Video encoding quality
VIDEO_CODEC = "libx264"
VIDEO_BITRATE = "2000k"  # Higher = better quality, larger files

# Audio encoding quality
AUDIO_CODEC = "aac"
AUDIO_BITRATE = "192k"

# Encoding speed preset
# Options: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
# ultrafast = fastest encoding, larger files
# veryslow = slowest encoding, best compression
ENCODING_PRESET = "medium"

# ============================================================================
# SUBTITLE SETTINGS
# ============================================================================

# Enable/disable subtitle generation
ENABLE_SUBTITLES = True

# Subtitle format
# Options: 'srt' (most compatible), 'vtt' (web), 'txt' (plain text)
SUBTITLE_FORMAT = "srt"

# Language detection
# Options: 'auto' (auto-detect), 'en', 'es', 'fr', 'de', 'hi', 'zh', 'ja', 'ko', 'ar', 'pt', 'ru', etc.
SUBTITLE_LANGUAGE = "auto"

# Whisper AI model size
# Options: 'tiny', 'base', 'small', 'medium', 'large'
# tiny:   Fastest, least accurate (~1GB RAM, ~32x realtime)
# base:   Fast, good accuracy (~1GB RAM, ~16x realtime) ⭐ RECOMMENDED
# small:  Slower, better accuracy (~2GB RAM, ~6x realtime)
# medium: Slow, great accuracy (~5GB RAM, ~2x realtime)
# large:  Slowest, best accuracy (~10GB RAM, ~1x realtime)
WHISPER_MODEL = "base"

# Burn subtitles into video?
# True = Hardcode subtitles permanently into video (recommended for social media)
# False = Keep subtitles as separate .srt files
BURN_SUBTITLES = True

# ============================================================================
# TRANSLATION SETTINGS (NEW!)
# ============================================================================

# Enable translation (translates subtitles to another language)
# Example: English video → English subtitles → Hindi translation
ENABLE_TRANSLATION = False

# Source language (language of the video/subtitles)
# Options: 'auto' (auto-detect), 'en', 'hi', 'es', 'fr', etc.
# If 'auto', will use the detected language from Whisper
TRANSLATION_SOURCE_LANG = "en"

# Target language (language to translate TO)
# Options: 'hi' (Hindi), 'en' (English), 'es' (Spanish), etc.
# Common Indian languages: 'hi', 'bn', 'te', 'ta', 'mr', 'gu', 'kn', 'ml', 'pa', 'ur'
TRANSLATION_TARGET_LANG = "hi"

# Create separate clips with translated subtitles?
# True = Create clips with both original AND translated subtitles
# False = Only create clips with translated subtitles (replaces original)
KEEP_ORIGINAL_SUBTITLES = False

# Translation output folder suffix
TRANSLATION_FOLDER_SUFFIX = "_translated"  # e.g., "clips_with_subtitles_translated"

# ============================================================================
# SUBTITLE STYLING (Applied when BURN_SUBTITLES = True)
# ============================================================================

# Font size (recommended: 20-36)
# 20-24: Small, for desktop viewing
# 24-28: Medium, good for mobile ⭐ RECOMMENDED
# 28-36: Large, best for TikTok/Reels
SUBTITLE_FONT_SIZE = 28

# Font name (system fonts)
# Common options: 'Arial', 'Helvetica', 'Verdana', 'Impact', 'Comic Sans MS'
# Leave as default for cross-platform compatibility
SUBTITLE_FONT_NAME = "Arial"

# Font color
# Options: 'white', 'yellow', 'black', 'red', 'green', 'blue', 'cyan', 'magenta'
# yellow = High visibility, great for social media ⭐ RECOMMENDED
# white = Clean, professional
SUBTITLE_FONT_COLOR = "yellow"

# Font outline/border color
# Options: 'black', 'white', 'none'
# Helps text stand out against any background
SUBTITLE_OUTLINE_COLOR = "black"

# Outline width (0-4)
# 0 = no outline
# 2 = medium outline ⭐ RECOMMENDED
# 4 = thick outline
SUBTITLE_OUTLINE_WIDTH = 2

# Background box behind text
# Format: "color@transparency"
# Examples:
#   "black@0.0"  = No background (transparent)
#   "black@0.5"  = 50% transparent black
#   "black@0.7"  = 70% transparent black ⭐ RECOMMENDED
#   "black@1.0"  = Solid black box
SUBTITLE_BG_COLOR = "black@0.7"

# Subtitle position
# Options: 'bottom', 'top', 'center'
SUBTITLE_POSITION = "bottom"

# Vertical margin from edge (in pixels)
# Higher number = more space from edge
SUBTITLE_MARGIN_V = 20

# Bold text
SUBTITLE_BOLD = True

# Italic text
SUBTITLE_ITALIC = False

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

# Enable detailed logging
ENABLE_LOGGING = True

# Log level
# Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
# DEBUG = Everything (most detailed)
# INFO = General information ⭐ RECOMMENDED
# WARNING = Only warnings and errors
# ERROR = Only errors
LOG_LEVEL = "INFO"

# Log to console (print to screen)
LOG_TO_CONSOLE = True

# Log to file
LOG_TO_FILE = True

# Log file name (will be in LOGS_FOLDER)
LOG_FILE_NAME = "video_processing.log"

# Maximum log file size (in MB) before rotation
LOG_MAX_SIZE_MB = 10

# Number of backup log files to keep
LOG_BACKUP_COUNT = 5

# Log format
# Don't modify unless you know what you're doing
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# ============================================================================
# PROCESSING OPTIONS
# ============================================================================

# Delete original clips after adding subtitles?
# True = Keep only clips with subtitles (saves space)
# False = Keep both versions
DELETE_ORIGINAL_CLIPS = False

# Delete downloaded YouTube video after processing?
# True = Save space
# False = Keep original download
DELETE_DOWNLOADED_VIDEO = False

# Maximum concurrent subtitle generation processes
# Higher = faster but uses more RAM
# 1 = Process one at a time (safest) ⭐ RECOMMENDED
# 2-4 = Faster if you have good CPU/RAM
MAX_CONCURRENT_PROCESSES = 1

# Skip clips that already have subtitles
SKIP_EXISTING_SUBTITLES = True

# ============================================================================
# BATCH PROCESSING (Multiple videos)
# ============================================================================

# List of YouTube URLs to process (leave empty if not batch processing)
BATCH_YOUTUBE_URLS = [
    # "https://youtu.be/VIDEO_ID_1",
    # "https://youtu.be/VIDEO_ID_2",
    # "https://youtu.be/VIDEO_ID_3",
]

# List of local video files to process
BATCH_LOCAL_FILES = [
    # "video1.mp4",
    # "video2.mp4",
    # "video3.mp4",
]

# ============================================================================
# ADVANCED SETTINGS (Rarely need to change)
# ============================================================================

# Create separate output folder for each video?
# True = Each video gets its own subfolder
# False = All clips in same folder
SEPARATE_FOLDERS_PER_VIDEO = False

# Clip naming format
# Available variables: {index}, {start}, {end}, {duration}
CLIP_NAME_FORMAT = "clip_{index:03d}_{start}s_to_{end}s"

# Include timestamp in folder names?
INCLUDE_TIMESTAMP_IN_FOLDERS = False

# Temporary files directory
TEMP_FOLDER = "temp"

# Clean up temporary files after processing?
CLEANUP_TEMP_FILES = True

# ============================================================================
# SOCIAL MEDIA PRESETS (Quick configurations)
# ============================================================================

# Uncomment one of these to quickly configure for specific platforms:

# # TikTok Preset
# CLIP_DURATION = 20
# SUBTITLE_FONT_SIZE = 32
# SUBTITLE_FONT_COLOR = "yellow"
# SUBTITLE_BG_COLOR = "black@0.7"
# SUBTITLE_POSITION = "bottom"
# BURN_SUBTITLES = True

# # Instagram Reels Preset
# CLIP_DURATION = 20
# SUBTITLE_FONT_SIZE = 28
# SUBTITLE_FONT_COLOR = "white"
# SUBTITLE_BG_COLOR = "black@0.6"
# SUBTITLE_POSITION = "bottom"
# BURN_SUBTITLES = True

# # YouTube Shorts Preset
# CLIP_DURATION = 30
# SUBTITLE_FONT_SIZE = 30
# SUBTITLE_FONT_COLOR = "yellow"
# SUBTITLE_BG_COLOR = "black@0.7"
# SUBTITLE_POSITION = "bottom"
# BURN_SUBTITLES = True

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def time_to_seconds(hours=0, minutes=0, seconds=0):
    """
    Convert time to seconds
    
    Examples:
        time_to_seconds(minutes=5, seconds=30)  # Returns 330
        time_to_seconds(hours=1, minutes=15)     # Returns 4500
    """
    return hours * 3600 + minutes * 60 + seconds


def create_all_directories():
    """Create all necessary directories"""
    directories = [
        OUTPUT_BASE_DIR,
        DOWNLOAD_PATH,
        CLIPS_PATH,
        CLIPS_WITH_SUBTITLES_PATH,
        SUBTITLE_FILES_PATH,
        LOGS_PATH,
    ]
    
    if CLEANUP_TEMP_FILES:
        directories.append(TEMP_FOLDER)
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)


def get_config_summary():
    """Get a summary of current configuration"""
    summary = {
        "Video Source": YOUTUBE_URL if YOUTUBE_URL else LOCAL_VIDEO_PATH,
        "Clip Duration": f"{CLIP_DURATION} seconds",
        "Subtitles Enabled": ENABLE_SUBTITLES,
        "Burn Subtitles": BURN_SUBTITLES if ENABLE_SUBTITLES else "N/A",
        "Subtitle Language": SUBTITLE_LANGUAGE if ENABLE_SUBTITLES else "N/A",
        "Whisper Model": WHISPER_MODEL if ENABLE_SUBTITLES else "N/A",
        "Font Size": SUBTITLE_FONT_SIZE if ENABLE_SUBTITLES else "N/A",
        "Font Color": SUBTITLE_FONT_COLOR if ENABLE_SUBTITLES else "N/A",
        "Output Directory": OUTPUT_BASE_DIR,
        "Logging Enabled": ENABLE_LOGGING,
    }
    return summary


# Auto-create directories when config is imported
create_all_directories()