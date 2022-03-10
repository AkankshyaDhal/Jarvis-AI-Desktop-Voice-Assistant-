
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
     engine.say(audio)
     print(audio)
     engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring akankshya!")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon ")

    else:
            speak("Good Evening ")

    speak("I am javis please tell me how may i help u")

def takeCommand():
   r=sr.Recognizer()
   with sr.Microphone() as source:
      print("Listening....")
      r.pause_threshold = 1 
      audio=r.listen(source)

   try:
     print("Recognizing...")
     query = r.recognize_google(audio,language='en-in')
     print(f"user said: {query}\n")

  
   except Exception as e:
       print("say that again please...")
       return "none"
   return query

def sendEmail(do,content):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login('akankshyadhal3874@gmail.com', '')
      server.sendmail('1841017095.c.akankshyadhal@gmail.com', to, content)
      server.close()


if __name__ == "__main__":

        speak("hello akankshya")
        wishMe()  
        
        # while True:  
        if 1:
             query=takeCommand().lower()
        
        #logic for executing tasks based on query
             if 'wikipedia' in query:
                   speak('Searching wikipedia....')
                   query= query.replace("wikipedia"," ")
                   result = wikipedia.summary(query, sentences =2)
                   speak("According to wikipedia")
                   print(result)
                   speak(result)
             elif 'open youtube' in query:
                 webbrowser.open('youtube.com')
             elif 'open google' in query:
                 webbrowser.open('google.com')
             elif 'open facebook' in query:
                 webbrowser.open('facebook.com')   
             elif 'open instagram' in query:
                 webbrowser.open('instagram.com')
             elif 'open linkedin' in query:
                 webbrowser.open('linkedin.com')
             elif 'open github' in query:
                 webbrowser.open('github.com')
             elif 'play music' in query:
                 music_dir="D:\\music"
                 songs = os.listdir(music_dir)
                 print(songs)
                 os.startfile(os.path.join(music_dir,songs[0]))
             elif 'the time' in query:
                 strTime = datetime.datetime.now().strftime("%H:%M:%S")
                 speak(f"aku,The time is {strTime}") 
        
             elif 'open code' in query:
                 codePath = "D:\\akankankshya software\Downloads\Microsoft VS Code\Code.exe"
                 os.startfile(codePath)
             elif 'send email' in query:
                 try:

                     speak["what should i say"]
                     content=takeCommand()   #takecommandreturnstring type 
                     to="1841017095.c.akankshyadhal@gmail.com"
                     sendEmail(to,content)
                     speak("Email has been sent!")
                 except Exception as e:
                     print(e)
                     speak("sorry aku ,mu mail send karipareleni")



             
