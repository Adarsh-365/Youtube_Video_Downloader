import streamlit as st
import yt_dlp
import os

# Directory to temporarily store downloaded videos
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Function to download video to server
def download_video(video_url, format_option="best"):
    ydl_opts = {
        "format": format_option,
        "outtmpl": os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
        "quiet": True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            file_path = ydl.prepare_filename(info)
            return file_path, info.get("title", "video")
    except Exception as e:
        return None, str(e)

# Streamlit app configuration for wide layout
st.set_page_config(page_title="YouTube Video Downloader", page_icon="🎥", layout="wide")

# Add title and description
st.title("🎥 YouTube Video Downloader")
st.write("Download Youtube Video of All sizes")

# Layout for full-width with 3 columns: margin, main content, margin
col1, col2, col3 = st.columns([1, 6, 1])

# Main content in the central column (col2)
with col2:
    # Input for video URL
    video_url = st.text_input("Enter YouTube Video URL:")

    # Quality options
    quality_option = st.selectbox("Choose Quality:", ["best", "bestaudio", "bestvideo"])

    # Button to download and prepare file
    if st.button("Get Video"):
        if not video_url.strip():
            st.error("Please enter a valid YouTube video URL.")
        else:
            with st.spinner("Getting video info ..."):
                file_path, video_title = download_video(video_url.strip(), quality_option)
            if file_path:
                st.success(f"Downloaded: {video_title}")
                
                # Provide the download button
                with open(file_path, "rb") as file:
                    st.download_button(
                        label="📥 Download Video",
                        data=file,
                        file_name=os.path.basename(file_path),
                        mime="video/mp4",
                    )
                
                # Delete the file after showing the download button
                if os.path.exists(file_path):
                    os.remove(file_path)
            else:
                st.error(f"Error: {video_title}")

# Footer (appears at the bottom of the page)
st.markdown("""
    <footer style="text-align:center; padding: 20px; background-color:#f1f1f1; font-size: 12px;">
        <p         style="color:blue;"> 2024 Your Company. All Rights Reserved.</p>
    </footer>
    """, unsafe_allow_html=True)
