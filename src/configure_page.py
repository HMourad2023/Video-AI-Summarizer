import streamlit as st

def configure_app_page():
    st.set_page_config(
        page_title="Video Summarizer",
        page_icon="🎥",
        layout="wide",
        initial_sidebar_state="collapsed"  
    )
    st.title("🎥 Video AI Summarizer")
