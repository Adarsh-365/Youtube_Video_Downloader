# YouTube Video Downloader 🎥

This is a Streamlit-based web application that allows users to download YouTube videos in various formats and qualities. 

## Features
- Download YouTube videos in different formats:
  - Best quality (`best`)
  - Audio-only (`bestaudio`)
  - Video-only (`bestvideo`)
- Easy-to-use interface with input fields and dropdowns.
- Full-width layout for a responsive user experience.
- Download button to save the video directly to your device.

## Requirements
- Python 3.8+
- Libraries:
  - `streamlit`
  - `yt-dlp`
  - `os`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (usually `http://localhost:8501`).

3. Enter the YouTube video URL, select the desired quality, and click "Get Video."

4. Once downloaded, use the download button to save the video to your device.

## File Structure
- `app.py`: The main Streamlit app script.
- `requirements.txt`: List of required Python libraries.

## Screenshot
![image](https://github.com/user-attachments/assets/2314f9e1-29af-488c-96ce-c65763453ec2)


## Notes
- Ensure the `downloads` directory has appropriate permissions for storing temporary video files.
- Downloaded files are automatically deleted after download to save disk space.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- [Streamlit](https://streamlit.io/) for the user interface framework.
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading functionality.

## Disclaimer
This application is for educational purposes only. Ensure you have the rights to download and use the content before proceeding.
