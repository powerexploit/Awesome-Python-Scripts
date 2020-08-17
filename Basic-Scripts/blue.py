import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sklearn
from gtts import gTTS
from pydub import audio_segment



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("My name is blu! how may i help u?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    WishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query :
            speak('searching Wikipedia..')
            query = query.replace("wikipedia", "")
            results = wikipedia.Summarry(query, sentence=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query :
            webbrowser.open("google.com")

        elif 'time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam! the time is {strTime}")

        elif 'play music' in query :
            speak("o k sir ! enjoy your song ")
            music_dir = 'C:\\Users\\Ankit Kumar\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'your intro' in query :
            WishMe()

        elif 'looking nice' in query :
            speak("thank u so much mam !, u looking beautyfull!")

        elif 'how are you' in query :
            speak("i am fine! and how are u?")

        elif 'i am also fine' in query :
            speak("o kay ! then lets start work ! what can i do for u?")

        elif 'nothing' in query :
            speak("o kay ! see u soon mam ! have a nice day !")

        elif 'hello brother' in query:
            speak("hello! daksh sir !")

        elif 'anything' in query :
            speak("do u want to play music?")

        elif 'stop this' in query:
            speak("are u sure sir?.")

        elif 'stop program' in query :
            break

        else:
            speak("thankyou sir! i am very happy to help you.")




