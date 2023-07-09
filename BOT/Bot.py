import pyttsx3
import speech_recognition as sr
import pywhatkit
import webbrowser
import pyaudio
import os
import wikipedia
import subprocess 
import sys
from AppOpener import open

yota=pyttsx3.init("sapi5")
voices=yota.getProperty("voices")
yota.setProperty("voices",voices[1].id)
yota.setProperty("rate",170)
def speak(audio):
    yota.say(audio)
    #print(f":")
    yota.runAndWait()
def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold=1
        audio=command.listen(source)
        try:
            print("Recognizing.....")
            query=command.recognize_google(audio,language="en-in")
            print(f"Master said:",query)
        except Exception as e:
            print("say that again")
            return "None"
        return query.lower()
def Taskexe():
    '''def Music():
        speak("tell the song,sir")
        Musicname=takecommand()
        if "HIH" in Musicname:
            os.startfile("Music")
        else:
            pywhatkit.playonyt(Musicname)
        speak("your song has been started,enjoy sir")'''
    def Main():
        if "close" in query:
            app_name=query.replace("close","").strip()
            close(app_name,match_closed)
        
                                
    while True:
        query=takecommand()
        if "hello" in query:
            speak("hello sir, iam YoTa")
            speak("your personal ai assistant")
            speak("how may i help you ")
        elif "how are you" in query:
            speak("iam fine sir")
            speak("what about you")
        elif "you need a break" in query:
            speak("okay sir,you can call me anytime")
            break
        elif "bye" in query:
            speak("okay sir bye")
            break
        elif "youtube search" in query:
            speak("okay sir,this is what i found for your search")
            query=query.replace("yota","")
            query=query.replace("youtube search","")
            web="https://www.youtube.com/results?search_query="+query    
            webbrowser.open(web)
            speak ("done sir")
        elif "google search" in query:
            speak("this is what i found for your search sir,")
            query=query.replace("yota","")
            query=query.replace("google search","")
            pywhatkit.search(query)
            speak("done sir")    
        elif "open website" in query:
            speak("tell me the name of the website,sir")
            name=takecommand()
            web="https://www."+name+".com"
            webbrowser.openweb 
            speak("done sir")
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("yota","")
            query=query.replace("wikipedia","")
            wiki=wikipedia.summary(query,2) 
            speak("according to wikipedia.(wiki)")
        elif "open chrome" in query:
            speak("lauching chrome,sir")
            openapps()

        elif "open Notepad" in query:
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.exe") 
            speak("lauching notepad,sir")   
Taskexe()