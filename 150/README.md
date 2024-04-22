# 跟我 150 天，保证你不看字母听懂英文剧

---

## Project Overview

This script, developed for processing video and audio data, automates the extraction of audio from video files, combines these audio tracks with images to create new video files, and ultimately merges multiple video files into a single output file.

### Workflow
1. **Randomize and Rename Video Clips**: Randomizes the order of video clips and renames them for processing.
2. **Extract Audio**: Extracts audio from each video clip.
3. **Generate Video from Images and Audio**: Combines each audio file with a corresponding image to create a new video clip.
4. **Merge Videos**: Merges all the newly created video clips into one final video file.

### Directory Structure
- `.\src\mp4`: Contains the original video clips.
- `.\mp3`: Stores extracted audio files from the video clips.
- `.\src\image`: Contains images used to create new video clips.
- `.\mp3_and_image`: Stores the final video clips created from the images and audio files.
- `.\output.mp4`: The final merged video output.

### How To Use
1. **Prepare Your Files**:
   - Place your original video files in the `.\src\mp4` directory.
   - Ensure that corresponding images are stored in `.\src\image`.

2. **Run the Script**:
   - Execute the script by running:
     ```
     python main.py
     ```

3. **Check Outputs**:
   - Extracted audio files will be available in `.\mp3`.
   - Individual video files created from images and audio are in `.\mp3_and_image`.
   - The final merged video will be located in the root directory as `.\output.mp4`.

### Installation
Ensure you have Python and moviepy installed:
```bash
pip install moviepy
```
