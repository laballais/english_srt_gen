# Configure Video Path Here
import os

# Get video name
def get_filename_without_extension(file_path):
    # Get the base name of the file (e.g., "video.mp4")
    base_name = os.path.basename(file_path)
    # Split the base name into the name and extension (e.g., "video" and ".mp4")
    file_name, _ = os.path.splitext(base_name)
    return file_name

# Input File
video_path = "./vlog.mp4"  # Input video file
video_name = get_filename_without_extension(video_path)

# Output Files 
audio_path = video_name + ".wav"  # Extracted audio file
srt_path = video_name + ".srt"  # Output SRT file