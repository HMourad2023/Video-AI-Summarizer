import streamlit as st
from src.agent import initialize_agent
from src.configure_page import configure_app_page
from src.preprocess_video import process_video
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Configure the Streamlit page
configure_app_page()

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    st.error("Missing Google API Key. Please define it in the .env file.")

@st.cache_resource
def get_agent():
    """Initialize the agent with caching."""
    return initialize_agent()

# Initialize the agent
agent = initialize_agent()

# Step 1: Upload the video
st.subheader("Step 1: Upload a video")
processed_video = process_video()

# Step 2: Ask the question if the video is uploaded
if processed_video:
    st.subheader("Step 2: Ask your question")
    user_query = st.text_area(
        "What insights are you seeking from the video?",
        placeholder="Ask anything about the video content. The AI agent will analyze and gather additional context if needed.",
        help="Provide specific questions or insights you want from the video."
    )

    # Step 3: Analyze the video if a question is asked and the button is clicked
    st.subheader("Step 3: Analyzing the video")
    if st.button("🔍 Analyze Video", key="analyze_video_button"):
        if not user_query:
            st.warning("Please enter a question or insight to analyze the video.")
        else:
            try:
                with st.spinner("Processing video and gathering insights..."):
                    # Generate the query for analysis
                    analysis_prompt = (
                        f"""
                        Analyze the uploaded video for content and context.
                        Respond to the following query using video insights and supplementary web research:
                        {user_query}

                        Provide a detailed, user-friendly, and actionable response.
                        """
                    )

                    # Run the AI agent
                    response = agent.run(analysis_prompt, videos=[processed_video])

                    # Display the result
                    st.subheader("Analysis Result")
                    st.markdown(response.content)
            
            except Exception as error:
                st.error(f"An error occurred during analysis: {error}")
else:
    st.info("Please upload a video to begin.")

