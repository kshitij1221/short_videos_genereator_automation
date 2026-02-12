"""
YouTube Video Downloader - Integrated with config and logging
Downloads YouTube videos for processing
"""

import os
import re
from pathlib import Path
import config
from logger import get_logger

logger = get_logger()

try:
    import yt_dlp
    YT_DLP_AVAILABLE = True
except ImportError:
    YT_DLP_AVAILABLE = False
    logger.warning("yt-dlp not installed. YouTube download functionality unavailable.")
    logger.info("Install with: pip install yt-dlp")


class YouTubeDownloader:
    def __init__(self, download_folder=None):
        """
        Initialize YouTube downloader
        
        Args:
            download_folder (str): Folder to save downloaded videos (uses config if None)
        """
        self.download_folder = download_folder or config.DOWNLOAD_PATH
        Path(self.download_folder).mkdir(parents=True, exist_ok=True)
        logger.debug(f"Download folder: {self.download_folder}")
    
    def is_youtube_url(self, url):
        """Check if the URL is a valid YouTube URL"""
        youtube_regex = (
            r'(https?://)?(www\.)?'
            '(youtube|youtu|youtube-nocookie)\.(com|be)/'
            '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
        )
        return re.match(youtube_regex, url) is not None
    
    def download_video(self, url, output_name=None, quality=None):
        """
        Download a YouTube video
        
        Args:
            url (str): YouTube video URL
            output_name (str): Custom output filename (optional)
            quality (str): Video quality (uses config if None)
        
        Returns:
            str: Path to downloaded video file, or None if failed
        """
        if not YT_DLP_AVAILABLE:
            logger.error("yt-dlp is not installed!")
            logger.info("Install it with: pip install yt-dlp")
            return None
        
        if not self.is_youtube_url(url):
            logger.error(f"Invalid YouTube URL: {url}")
            return None
        
        quality = quality or config.YOUTUBE_QUALITY
        
        logger.info(f"Downloading video from YouTube...")
        logger.info(f"URL: {url}")
        logger.info(f"Quality: {quality}")
        
        # Configure yt-dlp options
        if output_name:
            output_template = os.path.join(self.download_folder, output_name)
        else:
            output_template = os.path.join(self.download_folder, '%(title)s.%(ext)s')
        
        ydl_opts = {
            'format': self._get_format_string(quality),
            'outtmpl': output_template,
            'quiet': False,
            'no_warnings': False,
            'progress_hooks': [self._progress_hook],
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Get video info
                info = ydl.extract_info(url, download=False)
                video_title = info.get('title', 'video')
                duration = info.get('duration', 0)
                
                logger.info(f"Title: {video_title}")
                logger.info(f"Duration: {self._format_duration(duration)}")
                
                # Download the video
                info = ydl.extract_info(url, download=True)
                
                # Get the downloaded file path
                downloaded_file = ydl.prepare_filename(info)
                
                if os.path.exists(downloaded_file):
                    size_mb = os.path.getsize(downloaded_file) / (1024 * 1024)
                    logger.info(f"Download complete: {downloaded_file}")
                    logger.info(f"File size: {size_mb:.2f} MB")
                    return downloaded_file
                else:
                    logger.error("Downloaded file not found")
                    return None
                
        except Exception as e:
            logger.log_error_with_exception("Error downloading video", e)
            return None
    
    def _get_format_string(self, quality):
        """Convert quality setting to yt-dlp format string"""
        quality_map = {
            'best': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'worst': 'worst',
            '2160p': 'bestvideo[height<=2160]+bestaudio/best[height<=2160]',
            '1080p': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            '720p': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            '480p': 'bestvideo[height<=480]+bestaudio/best[height<=480]',
            '360p': 'bestvideo[height<=360]+bestaudio/best[height<=360]',
        }
        return quality_map.get(quality, quality_map['best'])
    
    def _progress_hook(self, d):
        """Progress hook for download status"""
        if d['status'] == 'downloading':
            try:
                percent = d.get('_percent_str', 'N/A')
                speed = d.get('_speed_str', 'N/A')
                eta = d.get('_eta_str', 'N/A')
                logger.debug(f"Download: {percent} | Speed: {speed} | ETA: {eta}")
            except:
                pass
        elif d['status'] == 'finished':
            logger.info("Download finished, processing...")
    
    def _format_duration(self, seconds):
        """Format duration in seconds to HH:MM:SS"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        if hours > 0:
            return f"{hours}h {minutes}m {secs}s"
        elif minutes > 0:
            return f"{minutes}m {secs}s"
        else:
            return f"{secs}s"
    
    def get_video_info(self, url):
        """
        Get information about a YouTube video without downloading
        
        Args:
            url (str): YouTube video URL
            
        Returns:
            dict: Video information
        """
        if not YT_DLP_AVAILABLE:
            logger.error("yt-dlp is not installed!")
            return None
        
        if not self.is_youtube_url(url):
            logger.error(f"Invalid YouTube URL: {url}")
            return None
        
        try:
            ydl_opts = {'quiet': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                return {
                    'title': info.get('title', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'duration_formatted': self._format_duration(info.get('duration', 0)),
                    'uploader': info.get('uploader', 'Unknown'),
                    'view_count': info.get('view_count', 0),
                    'description': info.get('description', ''),
                }
        except Exception as e:
            logger.log_error_with_exception("Error getting video info", e)
            return None
