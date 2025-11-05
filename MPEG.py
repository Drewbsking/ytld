import os
import subprocess

# Define input video files
video_files = ["vv01.mp4", "vv02.mp4"]
concat_file = "file_list.txt"  # Temporary file for FFmpeg input
output_file = "jake.mp4"


def create_concat_file(video_files, concat_file):
    """Create a text file listing videos in FFmpeg-compatible format."""
    with open(concat_file, "w") as f:
        for video in video_files:
            f.write(f"file '{video}'\n")
    print(f"[INFO] Created list file: {concat_file}")


def merge_videos(concat_file, output_file):
    """Use FFmpeg to merge videos without re-encoding."""
    cmd = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", concat_file, "-c", "copy", output_file]

    print(f"[INFO] Merging videos into {output_file}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"[SUCCESS] Merging completed: {output_file}")
    else:
        print(f"[ERROR] Failed to merge videos:\n{result.stderr}")


# Execute steps
create_concat_file(video_files, concat_file)
merge_videos(concat_file, output_file)

# Cleanup
os.remove(concat_file)
print(f"[INFO] Temporary file {concat_file} removed.")
