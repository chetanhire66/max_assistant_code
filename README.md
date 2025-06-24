# Max & Tom Voice Assistants 🎙️🤖

A dual AI-powered voice assistant system — **Max** (GPT + productivity) and **Tom** (news + speech interaction) — built with Python. They listen to your voice, fetch news, answer prompts using Gemini API, and perform smart browser actions.

## 🔧 Features

### Max Assistant
- Wake word: “Max”
- Uses Google Gemini API (`gemini-1.5-flash`) for AI replies
- Text-to-speech responses
- Voice command triggers for:
  - Google, YouTube, Instagram
  - College ERP, DBT site
  - Music playing via custom music library
  - AI-generated answers
  - Indian & US news using `.env` API keys

### Tom Assistant
- Wake word: “Tom”
- Simpler structure for beginners
- Fetches Indian headlines using [NewsData.io](https://newsdata.io/)
- Text-to-speech built with `pyttsx3`
- Voice interaction with `speech_recognition`

## 🛡️ API Key Handling (Secure with .env)
- Gemini API: `GEMINI_API_KEY`
- News API: `MAX_NEWS_API_KEY`
- Use a `.env` file and `python-dotenv` to keep your API keys hidden.

## 📂 Project Structure

max_assistant/
├── max.py
├── music_library.py
├── max_api_keys.env
├── README.md
├── .gitignore
└── ...

Copy
Edit
tom_assistant/
├── tom.py
├── tom_api_key.env
├── README.md
├── .gitignore
└── ...

markdown
Copy
Edit

## 🔒 .gitignore
Make sure `.env` and `__pycache__/` are ignored for security and cleanliness.

.env
*.env
pycache/
.vscode/
.idea/

markdown
Copy
Edit

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
Add .env file:

env
Copy
Edit
GEMINI_API_KEY=your_key_here
MAX_NEWS_API_KEY=your_news_api_key_here
Run the assistant:

bash
Copy
Edit
python max.py
# or
python tom.py
🛠️ Built With
Python 3.10+

speech_recognition

pyttsx3

requests

google.generativeai

dotenv

👨‍💻 Made by Vishal
Voice AI nerd. Loves automation, AIML, and low-budget innovation. Built for fun and future!
