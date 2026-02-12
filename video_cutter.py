"""
Video Cutter - Integrated with config and logging
Cuts long videos into short clips
"""

import ffmpeg
import os
from pathlib import Path
import config
from logger import get_logger

logger = get_logger()


class VideoCutter:
    def __init__(self, input_video, output_folder=None, clip_duration=None):
        """
        Initialize the video cutter
        
        Args:
            input_video (str): Path to the input video file
            output_folder (str): Folder to store output clips (uses config if None)
            clip_duration (int): Duration of each clip in seconds (uses config if None)
        """
        self.input_video = input_video
        self.output_folder = output_folder or config.CLIPS_PATH
        self.clip_duration = clip_duration or config.CLIP_DURATION
        
        # Create output folder if it doesn't exist
        Path(self.output_folder).mkdir(parents=True, exist_ok=True)
        logger.debug(f"Output folder created: {self.output_folder}")
    
    def get_video_duration(self):
        """Get the duration of the video in seconds"""
        try:
            probe = ffmpeg.probe(self.input_video)
            video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
            duration = float(probe['format']['duration'])
            logger.debug(f"Video duration: {duration:.2f} seconds")
            return duration
        except Exception as e:
            logger.log_error_with_exception("Error getting video duration", e)
            return None
    
    def cut_video_segments(self):
        """Cut video into multiple segments"""
        duration = self.get_video_duration()
        
        if duration is None:
            logger.error("Could not determine video duration")
            return []
        
        logger.info(f"Video duration: {duration:.2f} seconds")
        logger.info(f"Creating {self.clip_duration}-second clips...")
        
        # Calculate number of clips
        num_clips = int(duration // self.clip_duration)
        created_clips = []
        
        for i in range(num_clips):
            start_time = i * self.clip_duration
            output_file = os.path.join(
                self.output_folder, 
                config.CLIP_NAME_FORMAT.format(
                    index=i+1,
                    start=int(start_time),
                    end=int(start_time + self.clip_duration),
                    duration=self.clip_duration
                ) + ".mp4"
            )
            
            try:
                logger.log_video_cut(
                    os.path.basename(output_file),
                    start_time,
                    start_time + self.clip_duration
                )
                
                # Cut the video segment with audio
                (
                    ffmpeg
                    .input(self.input_video, ss=start_time, t=self.clip_duration)
                    .output(
                        output_file,
                        vcodec=config.VIDEO_CODEC,
                        acodec=config.AUDIO_CODEC,
                        audio_bitrate=config.AUDIO_BITRATE,
                        video_bitrate=config.VIDEO_BITRATE,
                        preset=config.ENCODING_PRESET
                    )
                    .overwrite_output()
                    .run(capture_stdout=True, capture_stderr=True, quiet=True)
                )
                
                logger.log_file_created(output_file)
                created_clips.append(output_file)
                
            except ffmpeg.Error as e:
                logger.error(f"Error creating clip {i+1}: {e.stderr.decode()}")
        
        # Handle remaining footage if any
        remaining_time = duration - (num_clips * self.clip_duration)
        if remaining_time > 5:  # Only create if remaining footage is more than 5 seconds
            start_time = num_clips * self.clip_duration
            output_file = os.path.join(
                self.output_folder,
                config.CLIP_NAME_FORMAT.format(
                    index=num_clips+1,
                    start=int(start_time),
                    end=int(duration),
                    duration=int(remaining_time)
                ) + ".mp4"
            )
            
            try:
                logger.info(f"Creating final clip: {os.path.basename(output_file)}")
                (
                    ffmpeg
                    .input(self.input_video, ss=start_time, t=remaining_time)
                    .output(
                        output_file,
                        vcodec=config.VIDEO_CODEC,
                        acodec=config.AUDIO_CODEC,
                        audio_bitrate=config.AUDIO_BITRATE,
                        video_bitrate=config.VIDEO_BITRATE,
                        preset=config.ENCODING_PRESET
                    )
                    .overwrite_output()
                    .run(capture_stdout=True, capture_stderr=True, quiet=True)
                )
                logger.log_file_created(output_file)
                created_clips.append(output_file)
            except ffmpeg.Error as e:
                logger.error(f"Error creating final clip: {e.stderr.decode()}")
        
        logger.info(f"All clips saved in: {self.output_folder}")
        return created_clips
    
    def cut_specific_segment(self, start_time, end_time=None, output_name="custom_clip.mp4"):
        """
        Cut a specific segment from the video
        
        Args:
            start_time (int/float): Start time in seconds
            end_time (int/float): End time in seconds (if None, uses start_time + clip_duration)
            output_name (str): Name of the output file
        """
        if end_time is None:
            duration = self.clip_duration
        else:
            duration = end_time - start_time
        
        output_file = os.path.join(self.output_folder, output_name)
        
        try:
            logger.info(f"Creating clip from {start_time}s to {start_time + duration}s...")
            
            (
                ffmpeg
                .input(self.input_video, ss=start_time, t=duration)
                .output(
                    output_file,
                    vcodec=config.VIDEO_CODEC,
                    acodec=config.AUDIO_CODEC,
                    audio_bitrate=config.AUDIO_BITRATE,
                    video_bitrate=config.VIDEO_BITRATE,
                    preset=config.ENCODING_PRESET
                )
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True, quiet=True)
            )
            
            logger.log_file_created(output_file)
            return output_file
            
        except ffmpeg.Error as e:
            logger.error(f"Error creating clip: {e.stderr.decode()}")
            return None
