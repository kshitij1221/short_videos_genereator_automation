# 🎬 Complete Video Cutter with Subtitles Package

## 📦 ALL FILES INCLUDED

This is the **COMPLETE PACKAGE** - everything you need to run!

### ✅ Core Files (Required)

1. **`run.py`** - Main script to execute
2. **`config.py`** - All your settings (EDIT THIS!)
3. **`logger.py`** - Logging system
4. **`video_cutter.py`** - Video cutting logic
5. **`youtube_downloader.py`** - YouTube download logic
6. **`subtitle_generator.py`** - Subtitle generation logic
7. **`requirements.txt`** - Python dependencies

### 📚 Documentation Files

8. **`SETUP_GUIDE.md`** - Complete setup instructions
9. **`SUBTITLE_GUIDE.md`** - Subtitle feature guide
10. **`YOUTUBE_SETUP.md`** - YouTube download guide

---

## 🚀 QUICK START (3 Commands!)

### 1. Install Dependencies
```bash
pip install ffmpeg-python yt-dlp openai-whisper
```

### 2. Edit Configuration
Open `config.py` and set your YouTube URL:
```python
YOUTUBE_URL = "https://youtu.be/YOUR_VIDEO_ID"
```

### 3. Run!
```bash
python run.py
```

**That's it!** Check `output/clips_with_subtitles/` for your clips!

---

## 📁 What Gets Created

After running, you'll have:

```
output/
├── downloads/              # Downloaded YouTube videos
├── clips/                  # Clips without subtitles
├── clips_with_subtitles/   # 🎉 FINAL CLIPS HERE!
├── subtitle_files/         # Separate .srt files
└── logs/                   # Processing logs
    └── video_processing.log
```

---

## ⚙️ Configuration Options (config.py)

### Video Source
```python
YOUTUBE_URL = "https://youtu.be/VIDEO_ID"  # YouTube URL
# OR
LOCAL_VIDEO_PATH = "my_video.mp4"  # Local file
```

### Clip Settings
```python
CLIP_DURATION = 20  # Seconds per clip
VIDEO_BITRATE = "2000k"  # Video quality
AUDIO_BITRATE = "192k"   # Audio quality
```

### Subtitle Settings
```python
ENABLE_SUBTITLES = True  # Turn on/off
BURN_SUBTITLES = True    # Hardcode into video
SUBTITLE_LANGUAGE = "auto"  # Auto-detect language
WHISPER_MODEL = "base"   # AI model size
```

### Subtitle Style
```python
SUBTITLE_FONT_SIZE = 28           # Font size (24-32 recommended)
SUBTITLE_FONT_COLOR = "yellow"    # Color
SUBTITLE_BG_COLOR = "black@0.7"   # Background with transparency
SUBTITLE_OUTLINE_COLOR = "black"  # Outline color
SUBTITLE_OUTLINE_WIDTH = 2        # Outline thickness
SUBTITLE_POSITION = "bottom"      # Position on screen
SUBTITLE_BOLD = True              # Bold text
```

---

## 📝 Logging

Everything is logged in detail!

**Log file location:** `output/logs/video_processing.log`

**What's logged:**
- ✅ Configuration used
- 📥 Download progress
- ✂️ Clip creation
- 📝 Subtitle generation
- 🔥 Subtitle burning
- ⏱️ Processing times
- ❌ Errors with details
- 📊 Final statistics

---

## 🎯 Social Media Presets

Quick configurations for popular platforms (uncomment in config.py):

### TikTok
```python
CLIP_DURATION = 20
SUBTITLE_FONT_SIZE = 32
SUBTITLE_FONT_COLOR = "yellow"
```

### Instagram Reels
```python
CLIP_DURATION = 20
SUBTITLE_FONT_SIZE = 28
SUBTITLE_FONT_COLOR = "white"
```

### YouTube Shorts
```python
CLIP_DURATION = 30
SUBTITLE_FONT_SIZE = 30
SUBTITLE_FONT_COLOR = "yellow"
```

---

## 🎨 Color Options

### Font Colors
- `white` - Clean, professional
- `yellow` - High visibility ⭐ RECOMMENDED
- `red` - Attention-grabbing
- `green` - Gaming content
- `blue` - Corporate
- `cyan` - Tech content
- `magenta` - Creative content

### Background Transparency
- `black@0.0` - No background (transparent)
- `black@0.5` - Light background
- `black@0.7` - Good balance ⭐ RECOMMENDED
- `black@0.9` - Heavy background
- `black@1.0` - Solid black box

---

## ⚡ Performance Tips

### For Speed
```python
WHISPER_MODEL = "tiny"      # Fastest model
YOUTUBE_QUALITY = '480p'    # Lower quality = faster download
ENABLE_SUBTITLES = False    # Skip subtitles for testing
```

### For Quality
```python
WHISPER_MODEL = "medium"    # Better accuracy
YOUTUBE_QUALITY = '1080p'   # Higher quality
VIDEO_BITRATE = "5000k"     # Better video quality
```

### Save Disk Space
```python
DELETE_ORIGINAL_CLIPS = True      
DELETE_DOWNLOADED_VIDEO = True    
```

---

## 🔧 Troubleshooting

### Error: "Module not found"
**Solution:** Install dependencies
```bash
pip install ffmpeg-python yt-dlp openai-whisper
```

### Error: "FFmpeg not found"
**Solution:** Install FFmpeg on your system
- **Windows:** `choco install ffmpeg`
- **Mac:** `brew install ffmpeg`
- **Linux:** `sudo apt install ffmpeg`

### Subtitles not visible
**Solution:** Increase contrast
```python
SUBTITLE_FONT_SIZE = 32
SUBTITLE_FONT_COLOR = "yellow"
SUBTITLE_BG_COLOR = "black@0.9"
```

### Out of memory
**Solution:** Use smaller model
```python
WHISPER_MODEL = "tiny"  # or "base"
```

### Check logs for details
```bash
cat output/logs/video_processing.log
```

---

## 📊 What You Get

### Input
- YouTube URL or local video file

### Processing
1. ✅ Download (if YouTube)
2. ✅ Cut into clips
3. ✅ Generate subtitles
4. ✅ Burn subtitles into video
5. ✅ Organize in folders
6. ✅ Log everything

### Output
- Clips without subtitles → `output/clips/`
- Clips WITH subtitles → `output/clips_with_subtitles/` 🎉
- Subtitle files → `output/subtitle_files/`
- Processing logs → `output/logs/`

---

## 💡 Use Cases

Perfect for:
- ✅ TikTok content creation
- ✅ Instagram Reels
- ✅ YouTube Shorts
- ✅ Podcast highlights
- ✅ Webinar clips
- ✅ Educational content
- ✅ Marketing videos
- ✅ Social media automation

---

## 🎓 Example Workflow

```bash
# 1. Install once
pip install ffmpeg-python yt-dlp openai-whisper

# 2. Edit config.py
# Set YOUTUBE_URL = "your_video_url"

# 3. Run
python run.py

# 4. Wait for processing (check logs for progress)
# Logs are in: output/logs/video_processing.log

# 5. Get your clips!
# Final clips in: output/clips_with_subtitles/

# 6. Upload to social media!
```

---

## 📈 Processing Time Estimates

**For 1-hour video:**

| Model | Subtitle Time | Total Time |
|-------|--------------|------------|
| tiny  | ~10 min      | ~15 min    |
| base  | ~15 min      | ~20 min ⭐ |
| small | ~30 min      | ~35 min    |
| medium| ~60 min      | ~65 min    |

*With GPU: 3-10x faster!*

---

## 🌍 Supported Languages

Whisper supports 100+ languages including:
- English, Spanish, French, German, Italian
- Portuguese, Hindi, Chinese, Japanese, Korean
- Arabic, Russian, and many more!

Use `SUBTITLE_LANGUAGE = "auto"` for automatic detection!

---

## 💰 Cost

**100% FREE!**
- ✅ No API keys needed
- ✅ No subscriptions
- ✅ No usage limits
- ✅ Open source

---

## ✨ Features Summary

- ✂️ Automatic video cutting
- 📥 YouTube download support
- 📝 FREE subtitle generation
- 🔥 Burn subtitles into videos
- 🌍 100+ languages
- 🎨 Customizable styling
- 📁 Organized folders
- 📊 Detailed logging
- ⚙️ Fully configurable
- 🚀 Production ready

---

## 📞 Support

If you encounter issues:
1. Check the log file: `output/logs/video_processing.log`
2. Review `SETUP_GUIDE.md` for detailed instructions
3. Ensure all dependencies are installed
4. Verify FFmpeg is installed on your system

---

## 🎉 Ready to Go!

You have everything you need. Just:
1. Install dependencies
2. Edit config.py
3. Run: `python run.py`

Happy content creating! 🎬✨
