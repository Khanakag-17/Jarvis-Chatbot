import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests

r = sr.Recognizer()
engine = pyttsx3.init()

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2025-01-16&'
       'sortBy=popularity&'
       'apiKey=bfbe67cc228b4e1ca4e0daa76b2002cb')
response = requests.get(url)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(text):
    song = text.lower.split(" ")[1]
    print(text)
    if 'open google' in text.lower():
        webbrowser.open("https://google.com")
    elif 'open facebook' in text.lower():
        webbrowser.open("https://facebook.com")
    elif 'open linkedin' in text.lower():
        webbrowser.open("https://linkedin.com")
    elif 'open youtube' in text.lower():
        webbrowser.open("https://youtube.com")

    elif text.lower().startswith("play") or music_library.music[song] in text.lower():
        music_library.music[song]

    elif 'news' in text.lower():
        if response.status_code == 200:
            data = response.json()
            # Extract and print all headlines
            for article in data.get('articles', []):
                print(article.get('title'))

    else: print("Can't process request.")

if (__name__ == "__main__"):
    speak("Jarvis initialized....")

    #Answering only when make call initiated - 'Jarvis'
    while True:  
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout = 2, phrase_time_limit= 2)

            print("Recognizing....")

            word = r.recognize_google(audio)
            if word.lower() == 'jarvis':
                speak("Ya")

                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout = 2, phrase_time_limit= 2)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error".format(e))