# subtitle_translator
Instantly translate your video's  subtitles into any language with the accuracy of Google Cloud.
# Video Subtitle Translator

Video Subtitle Translator is a Python application that uses the Google Cloud Translation API to automatically translate .vtt subtitle files into Turkish or any other language supported by Google Cloud, and then embeds them into the specified video.


## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contribution](#contribution)
- [License](#license)

## Features

- **Fast Translation:** Uses Google Cloud Translation API for quick and accurate results.
- **Support for Multiple Languages:** Translates subtitles into any language supported by Google Cloud.
- Directly embeds the translated subtitles into the video.

## Requirements

- Python 3.x
- [FFmpeg](https://ffmpeg.org/download.html)
- A Google Cloud account with the Translation API enabled and credentials downloaded.
- Necessary Python libraries which are listed in `requirements.txt`.


## Installation

1. **Clone the Repository:** Start by cloning the repository to your local machine.
   ```bash
   git clone https://github.com/muhammedozdemir57/subtitle_translator.git
   ```

2. **Navigate to the Directory:** Change to the project directory.
   ```bash
   cd subtitle_translator
   ```

3. **Install the Required Python Library:**
   ```bash
   pip install google-cloud-translate==2.0.1
   ```

4. **Download and Install FFmpeg:** Make sure [FFmpeg](https://ffmpeg.org/download.html) is installed and added to your system's path.

5. **Setup Google Cloud Translation API:** Follow the [official documentation](https://cloud.google.com/translate/docs/setup) to enable the Translation API. Download the credentials JSON and place it in the project's root directory. Update the path in `main.py` accordingly.

## Usage

- **Place Your Video and Subtitle Files:** Ensure your video file is named `video.mp4` and your subtitle file is `subtitle.vtt` (or modify the script to match your filenames).
- **Update the Google Cloud Credentials Path:** Adjust the path in `main.py` to your Google Cloud credentials JSON.
- **Execute the Script:** Start the automatic translation and embedding process with the command:
   ```bash
   python main.py
   ```

## Contribution
Feel free to fork, improve, make pull requests or fill issues. I'll appreciate any sort of contribution!

## License
This project is under the MIT License. Please refer to the [LICENSE](LICENSE) file for more details.
```




