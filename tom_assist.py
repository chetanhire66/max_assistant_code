from dotenv import load_dotenv
import os

import speech_recognition as sr

import pyttsx3
import webbrowser
import requests

load_dotenv=("tom_api_key.env")

api_key=os.getenv("TOM_NEWS_API_kEY")

recognizer=sr.Recognizer()
def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# def getnews():
#     # url = "https://imdb8.p.rapidapi.com/news/v2/get-by-category"

    # querystring = {
    #     "category": "MOVIE",
    #     "first": "5",              # Limiting to top 5 results
    #     "country": "US",
    #     "language": "en-US"
    # }

    # headers = {
    #     "x-rapidapi-key": "fdd31ca44fmshc59c59c3779c03cp1b8301jsnb7949d2157db",
    #     "x-rapidapi-host": "imdb8.p.rapidapi.com"
    # }

    # try:
    #     response = requests.get(url, headers=headers, params=querystring)
    #     if response.status_code == 200:
    #         data = response.json()
    #         articles = data.get("news", [])
    #         if articles:
    #             speak("Here are the top 5 movie news headlines from IMDb.")
    #             for i, article in enumerate(articles, 1):
    #                 headline = article.get("headline", {}).get("plainText", "No title")
    #                 print(f"{i}. {headline}")
    #                 speak(headline)
    #         else:
    #             speak("No movie news found at the moment.")
    #     else:
    #         print("Error:", response.status_code, response.text)
    #         speak("Failed to fetch movie news.")
    # except Exception as e:
    #     print("Exception while fetching IMDb news:", e)
    #     speak("Sorry, something went wrong while getting the movie news.")



# getnews()   

# def processcommand(c):
#     c=c.lower()
#     print("Proceesing command")
#     if "news" in c:
#         news_api = "60a925f2b6854cc08f835082f0949fea"
#         try:
#             r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}")
#             data = r.json()
#             if data["status"] == "ok":
#                 articles = data["articles"]
#                 speak("Here are the top 5 news headlines.")
#                 for i, article in enumerate(articles[:5], 1):
#                     speak(f"{i}. {article['title']}")
#             else:
#                 speak("Failed to fetch news.")
#         except Exception as e:
#             print("News error:", e)
#             speak("Could not fetch news right now.")
        


    # elif "exit" in c or "close" in c or "shutdown" in c:
    #         speak("Shutting down. Goodbye!")
    #         exit()
    # else:
    #     print("I didnt understood your command")
    #     speak("I didnt understood your command")   
    # 
def processcommand(c):
    c = c.lower()
    print("Processing command")

    if "news" in c:
        # Use NewsData.io for India headlines
        url = f"https://newsdata.io/api/1/news?apikey={api_key}&country=in&language=en"

        try:
            response = requests.get(url)
            data = response.json()

            if data.get("status") == "success":
                articles = data.get("results", [])
                if articles:
                    speak("Here are the top 5 news headlines from India.")
                    for i, article in enumerate(articles[:5], 1):
                        headline = article.get("title", "No title available")
                        print(f"{i}. {headline}")
                        speak(headline)
                else:
                    speak("No news articles found at the moment.")
            else:
                speak("Failed to fetch news from NewsData.")
        except Exception as e:
            print("News error:", e)
            speak("An error occurred while fetching the news.")
    
    elif "exit" in c or "close" in c or "shutdown" in c:
        speak("Shutting down. Goodbye!")
        exit()
    else:
        print("I didn’t understand your command")
        speak("I didn’t understand your command")
                
        

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()



       
   
if __name__=="__main__":
    speak("Starting Tom")
    with sr.Microphone() as source:
        print("Initailaizing Operations")
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print("Tom is ready to activate.Say Tom for activation")
        while True:
                try:
                    print("Listening wake word....")
                    audio=recognizer.listen(source,timeout=6,phrase_time_limit=5)
                    word=recognizer.recognize_google(audio)
                    print("You said : ",word)

                    if "tom" in word.lower():
                        speak("Listening for requests")
                        audio=recognizer.listen(source,timeout=6,phrase_time_limit=5)
                        order=recognizer.recognize_google(audio)
                        print("Command:", order)
                        processcommand(order)

                    else:
                        print("Wake word not detected")
                except Exception as e:
                    print("khatam",e)        


                    







    

#     import requests
# import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()

# def get_india_news():
#     url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=60a925f2b6854cc08f835082f0949fea"

#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             articles = data.get("articles", [])
#             if articles:
#                 speak("Here are the top news headlines from India.")
#                 for i, article in enumerate(articles[:5], 1):  # Limit to top 5
#                     headline = article.get("title", "No title available")
#                     print(f"{i}. {headline}")
#                     speak(headline)
#             else:
#                 speak("Sorry, no Indian news articles were found.")
#         else:
#             speak(f"Failed to fetch news. Status code {response.status_code}")
#             print("Error:", response.text)
#     except Exception as e:
#         print("Exception occurred:", e)
#         speak("An error occurred while fetching the news.")

# # Run it
# get_india_news()
