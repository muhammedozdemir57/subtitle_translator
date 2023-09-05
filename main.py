import subprocess
import os
from google.cloud import translate_v2 as translate

# Update this path for your authentication file.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "YOUR_PATH_HERE"

def translate_text(text, target_language="tr"):
    """Translates the provided text to the target language using Google Cloud API."""
    client = translate.Client()
    result = client.translate(text, target_language=target_language)
    return result["translatedText"]

def translate_subtitle(subtitle_path):
    with open(subtitle_path, 'r', encoding='utf-8') as file:
        subtitle_content = file.readlines()

    translated_content = []
    for line in subtitle_content:
        stripped_line = line.strip()
        # Avoid translating timestamps and numeric headers in .vtt files
        if stripped_line and not '-->' in stripped_line and not stripped_line[0].isdigit():
            translated_line = translate_text(stripped_line) + "\n"
            translated_content.append(translated_line)
        else:
            translated_content.append(line)

    translated_subtitle_path = "translated_" + subtitle_path
    with open(translated_subtitle_path, 'w', encoding='utf-8') as file:
        file.writelines(translated_content)

    return translated_subtitle_path

def embed_subtitle_to_video(video_path, subtitle_path):
    # Update the output_path according to where you want the video to be saved
    output_path = "C:\\Users\\YOUR_USERNAME_HERE\\Desktop\\YourDirectory\\output_video.mp4"
    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f'subtitles={subtitle_path}',
        output_path
    ]
    subprocess.run(cmd)
    return output_path

if __name__ == "__main__":
    video_file = 'index.mp4'
    subtitle_file = 'subtitles-en.vtt'

    if os.path.exists(video_file) and os.path.exists(subtitle_file):
        translated_subtitle = translate_subtitle(subtitle_file)
        output_video = embed_subtitle_to_video(video_file, translated_subtitle)
        print(f"Translated video saved at: {output_video}")

        # Remove original video, subtitle, and translated subtitle files after embedding
        os.remove(video_file)
        os.remove(subtitle_file)
        os.remove(translated_subtitle)  
    else:
        print("Video or subtitle file not found. Please ensure the files are in the correct location.")
