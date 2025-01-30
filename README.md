## 🎥 Phidata Video AI Summarizer

## 🎯 Description
Video AI Summarizer is a powerful application that leverages Gemini 2.0 Flash Exp AI to analyze and extract insights from video content. This tool allows users to upload videos and ask specific questions about their content, receiving detailed AI-powered analyses and summaries. Additionally, the agent can utilize tools like DuckDuckGo to perform web searches related to the video, providing supplementary context and enhanced insights.

## ⭐ Features
- **Video Upload & Processing**
- **AI-Powered Video Content Analysis**
- **Question-Based Insights Extraction**
- **Real-Time Processing Status Updates**
- **User-Friendly Interface**
- **Responsive Design**
- **Integration with Gemini 2.0 Flash Exp AI**

## 🛠️ Technologies Used
- ** Python 3.x**
- ** Streamlit** - Web interface
- ** Google Generative AI** - Video analysis
- ** Phidata** - AI agent implementation
- ** DuckDuckGo Tool** - Supplementary web research
- ** Python-dotenv** - Environment variables management

## 📋 Prerequisites
-  Python 3.x installed
-  Google API key for Gemini AI
-  Internet connection
-  Conda virtual environment **agenticai**

## 💻 Installation

1. Clone the repository:
```bash
 git clone https://github.com/yourusername/video-summarizer.git
 cd video-summarizer
```

2. Activate the **agenticai** virtual environment:
```bash
 conda activate agenticai
```

3. Install required dependencies:
```bash
 pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your **Google API Key**:
```env
 GOOGLE_API_KEY=your_api_key_here
```

## 🚀 Usage

1. Start the application:
```bash
 streamlit run app.py
```

2. 🌐 Open your browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Follow the **three-step process**:
   - **Upload your video**
   - **Enter your question** about the video content
   - **Click "Analyze Video"** to receive AI-generated insights

## 📁 Project Structure
```
video-summarizer/
├── app.py                     # Main application file
├── src/
│   ├── agent.py               # AI agent configuration
│   ├── configure_page.py      # Streamlit page setup
│   ├── preprocess_video.py    # Video upload and processing
├── .github/                   # GitHub-specific files
├── LICENSE                    # Project license
├── README.md                  # Project documentation
├── .env                       # Environment variables
└── requirements.txt           # Project dependencies
```

## ⚙️ Configuration
The application can be configured through the following files:
- `.env`: Environment variables including API keys
- `src/configure_page.py`: Streamlit page settings

## 🔑 Environment Variables
- `GOOGLE_API_KEY`: Your Google API key for Gemini AI

## 📜 License
This project is licensed under the **MIT License**.

## ✍️ Authors
- **Mourad Hamzaoui** - Data Scientist

## 🙏 Acknowledgments
- 🤖 **Gemini AI** for video analysis capabilities
- ⚙️ **Phidata** for AI agent framework
- 🌐 **Streamlit** for web application framework
