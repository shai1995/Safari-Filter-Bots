import os
from moviepy.editor import VideoFileClip

def generate_screenshots(video_path, output_dir, num_screenshots=10):
    """
    Generate screenshots from a video file.

    :param video_path: Path to the input video file
    :param output_dir: Directory where screenshots will be saved
    :param num_screenshots: Total number of screenshots to generate
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the video file
    clip = VideoFileClip(video_path)

    # Calculate the intervals at which to take screenshots
    total_duration = clip.duration
    interval = total_duration / (num_screenshots + 1)

    screenshots = []

    for i in range(num_screenshots):
        # Calculate the time for each screenshot
        screenshot_time = interval * (i + 1)
        screenshot_path = os.path.join(output_dir, f'screenshot_{i + 1}.png')
        clip.save_frame(screenshot_path, t=screenshot_time)
        screenshots.append(screenshot_path)

    return screenshots

# Example usage
if __name__ == "__main__":
    video_file = "path/to/your/video.mp4"  # Replace with your video file path
    output_directory = "screenshots"  # Output directory for screenshots
    screenshots = generate_screenshots(video_file, output_directory)
    print(f"Generated screenshots: {screenshots}")
