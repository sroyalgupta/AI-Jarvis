from win32com.client import Dispatch
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import random
import smtplib
from automated import show_assignment,calculate_attendance

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
d={'sagar':'sroyalgupta@gmail.com',
    'papa':'guptasureshchand1965@gmail.com',
    'parth' : 'parthvaidya99@gmail.com',
    'aakash' : 'aakashkhatu1998@gmail.com',
    'ajesh' : 'iam@ajesh.dev',
    'ashutosh' : 'ashu.atiwa@gmail.com'
    }
r = sr.Recognizer()
speak = Dispatch("SAPI.SpVoice")
def take_command():
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio_data = r.record(source, duration=5)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio_data,language='en-in')
            print(f"Your query : {text}")
        except:
            print("Sorry Say that again")
            return "None"
    return text

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sagarguptasargam123@gmail.com','srg@2909')
    server.sendmail('sagarguptasargam123@gmail.com',to,content)
    server.close()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak.Speak("Good Morning!")
    elif hour>12 and hour<17:
        speak.Speak("Good Afternoon!")
    else:
        speak.Speak("Good Evening!")
    speak.Speak("Hii I am Computer Baba, how can I help you!")

wish()
while True:
    query = take_command().lower()
    if 'wikipedia' in query:
        print("Searching Wikipedia")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        print(results)
        speak.Speak("Searching in Wikipedia")
        speak.Speak(results)

    elif 'open youtube' in query:
        webbrowser.get(chrome_path).open("youtube.com")

    elif 'open google' in query:
        webbrowser.get(chrome_path).open("google.com")

    elif 'play music' in query:
        songs_dir = "D://songs"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir,songs[random.randint(1,30)]))
    
    elif 'the time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        speak.Speak(f"Sir,the time is {time}")

    elif 'open code' in query:
        code_path = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)

    elif 'email' in query:
        try:
            speak.Speak("To whom would you like to send an email?")
            temp = take_command()
            to = d[temp]
            speak.Speak("Please tell your message")
            content = take_command()
            sendmail(to,content)
        except Exception as e:
            print(e)
    
    elif 'attendance' in query:
        attendance = calculate_attendance()
        print(attendance)
        speak.Speak(f"Your overall attendance is {attendance}")
    
    elif 'erp' in query:
        speak.Speak("Opening your erp,please wait...")
        temp = show_assignment()
