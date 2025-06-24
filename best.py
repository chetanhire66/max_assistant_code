import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import google.generativeai as genai
import os
from dotenv import load_dotenv




load_dotenv("max_api_keys.env")
api_key_1=os.getenv("GEMINI_API_KEY")
api_key_2=os.getenv("MAX_NEWS_API_KEY")
recognizer = sr.Recognizer()
s = pyttsx3.init()

def speak(text):
    s.say(text)
    s.runAndWait()

def aiprocess(command):
    # import google.generativeai as genai

# Configure your API key
    genai.configure(api_key=f"{api_key_1}")  #  Replace with your own key, never share it!

    # Use the free-tier Gemini 1.5 Flash model
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    # Ask a prompt
    prompt = command           #"Explain how backend of a website works"

    response = model.generate_content(command)

    # full_response=response.text
    # limited_lines="\n".join(full_response.split()[:4])     #Uncomment this for short response
    # print(limited_lines)

    # Print the response
    
    speak(response.text)
    print(f"{response.text}")

# def fetch_india_news():
#     url = "https://real-time-news-data.p.rapidapi.com/topic-news"

#     querystring = {
#         "topic": "WORLD",     # You can also try "WORLD", "POLITICS", "TECHNOLOGY"
#         "lang": "en",
#         "country": "us",
#         "limit": "5"
#     }

#     headers = {
#         "x-rapidapi-key": "fdd31ca44fmshc59c59c3779c03cp1b8301jsnb7949d2157db",
#         "x-rapidapi-host": "real-time-news-data.p.rapidapi.com"
#     }

#     try:
#         response = requests.get(url, headers=headers, params=querystring)
#         if response.status_code == 200:
#             data = response.json()
#             articles = data.get("data", [])
#             if articles:
#                 speak("Here are the top 5 news headlines from India.")
#                 for i, article in enumerate(articles, 1):
#                     headline = article.get("title", "No title")
#                     print(f"{i}. {headline}")
#                     speak(headline)
#             else:
#                 speak("No news found at the moment.")
#         else:
#             print("Error:", response.status_code, response.text)
#             speak("Failed to fetch Indian news.")
#     except Exception as e:
#         print("Exception while fetching news:", e)
#         speak("Sorry, something went wrong while getting the news.")    



def processcommand(c):
    c = c.lower()
    

    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c:
        webbrowser.open('https://www.instagram.com/vishal71342/')
    
    elif "jerk" in c or "Prabhu" in c:
        speak("The biggest jerk of all time who watches cartoons and studies in topmost college. Possibly born Chinese or Nepali.")
        webbrowser.open("https://www.instagram.com/prabhu._bankar")

    elif any(x in c for x in ["chetan", "turtle"]):
        speak("Opening Chetan ID")
        webbrowser.open("https://www.instagram.com/chetan_hire_66/")

    elif "jay" in c:
        speak("Opening Jay's profile")
        webbrowser.open("https://www.instagram.com/_jaywardhan_dange_/")

    elif "wall" in c:
        speak("The most beautiful and sublime soul of all time. Opening thy reflection.")
        webbrowser.open("https://www.instagram.com/sarah.d_07/")

    elif "open x" in c:
        webbrowser.open("https://mahadbt.maharashtra.gov.in/Login/Login")

    elif "open python" in c:
        webbrowser.open("https://youtu.be/UrsmFxEIp5k")

    elif "open college" in c:
        webbrowser.open("https://moderncoe.edu.in/")

    elif "open system" in c:
        webbrowser.open("https://erp.moderncoe.edu.in/login.aspx")

    elif "open marathi" in c:
        webbrowser.open("https://youtu.be/DrheZ7300pw")

    elif c.startswith("play"):
        parts = c.split(" ")
        if len(parts) > 1:
            song = parts[1]
            link = music_library.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("Sorry, I couldn't find that song.")
        else:
            speak("Please say the song name after play.")

    elif "news" in c:
        
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_2}")
            data = r.json()
            if data["status"] == "ok":
                articles = data["articles"]
                speak("Here are the top 5 news headlines.")
                for i, article in enumerate(articles[:5], 1):
                    speak(f"{i}. {article['title']}")
            else:
                speak("Failed to fetch news.")
        except Exception as e:
            print("News error:", e)
            speak("Could not fetch news right now.")
        
    elif "exit" in c or "close" in c or "shutdown" in c:
            speak("Shutting down. Goodbye!")
            exit()       
    else:
        aiprocess(command)
        # speak(w)         

# Main Loop
if __name__ == "__main__":
    speak("Starting Max")
    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Max is ready. Say 'Max' to activate.")

        while True:
            try:
                print("\nListening for wake word...")
                audio = recognizer.listen(source, timeout=6, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                print("You said:", word)

                if "max" in word.lower():
                    speak("How can I help you?")
                    print("Listening for your command...")
                    audio = recognizer.listen(source, timeout=6, phrase_time_limit=8)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    processcommand(command)
                else:
                    print("Wake word not detected.")

            except Exception as e:
                print("khatam:", e)
