import streamlit as st
from google.generativeai import upload_file, get_file
import tempfile
import os
import time

def process_video():
    video_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    
    if video_file:
        # Temporary storage of the uploaded video file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(video_file.read())
            temp_file_path = temp_file.name
        
        st.success(f"Video uploaded successfully")

        # Upload the video file
        processed_video = upload_file(temp_file_path)

        # Check the file status: wait for the processing to finish
        #st.info("Processing the uploaded video...")
        while processed_video.state.name == "PROCESSING":
            time.sleep(1)
            processed_video = get_file(processed_video.name)

        if processed_video.state.name == "ACTIVE":
            st.success("The video is now active and ready for analysis.")
            return processed_video
        else:
            st.error("The video processing failed or did not become active.")
            return None
    
    return None

