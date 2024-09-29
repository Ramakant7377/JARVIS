
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import wolframalpha
import os
import smtplib
import pywhatkit as wk
import pyautogui
import time


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate',180)

def speak(audio):
  engine.say(audio) 
  engine.runAndWait()

def wishme():
  hour = int(datetime.datetime.now().hour)
  if(hour>=0 and hour<12):
    speak("Good Morning!")

  elif hour>=12 and hour<18:
    speak("Good Afternoon!")

  else:
    speak("Good Evening!")  
  speak("I am JARVIS sir. Please tell me how may I help you")



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source) # `,phrase_time_limit=3` -- The ``phrase_time_limit`` parameter is the maximum number of seconds that this will allow a phrase to continue before stopping and returning the part of the phrase processed before the time limit was reached. The resulting audio will be the phrase cut off at the time limit. If ``phrase_timeout`` is ``None``, there will be no phrase time limit.


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tiwariramakant1001@gmail.com', 'your-password')
    server.sendmail('tiwariramakant1001@gmail.com', to, content)
    server.close() 

app = wolframalpha.Client("UQXHEE-UXK4TGK8JT")    
#speak("This is echo here!")
if __name__=="__main__" :
   wishme()
   while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case
        # if 'jarvis' in query:
        #     print("yes Sir")
        #     speak("Yes Sir") 

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open("youtube.com")   

        elif 'open youtube' in query:
            speak("what you will like to watch ?")
            qrry = takeCommand().lower()
            wk.playonyt(f"{qrry}") 

        elif 'search on youtube' in query:
            query = query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/results?search_querry={query}")       

        elif 'just open google' in query:
            webbrowser.open("google.com")

        elif 'open google' in query:
            speak("sir, What should i search on google")
            qry=takeCommand().lower()
            # webbrowser.open("google.com/?#q="+cm) 
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=1)
            speak(results)   
            

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")   

        elif 'close spotify' in query:
            os.system("taskkill/f /im spotify.exe")       

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            
            os.startfile(os.path.join(music_dir, songs[0]))         

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")    

        elif 'open code' in query:
            codePath = "C:\\Users\\Ramakant tiwari\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        # elif 'close code' in query:
        #     os.system("taskkill/f /im Code.exe")     

        elif 'email to Ramakant' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tiwariramakant1001@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Ramakant bhai. I am not able to send this email") 

        elif 'temperature' in query:
            res = app.query(query)
            speak(next(res.results).text)

        elif 'calculate' in query:
            speak('what should i calculate?')  
            gh = takeCommand().lower()
            res = app.query(gh)
            speak(next(res.results).text)  

        # elif 'play songs on youtube' in query:
        #     pywhatkit.playonyt("see you again") 

        if 'open chrome' in query:
            os.startfile("C:\\Users\\Ramakant tiwari\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")

        elif 'maximize this window' in query:
            pyautogui.hotkey('alt','space')
            time.sleep(1)
            pyautogui.press('x')

        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt','d')
            pyautogui.write(f"{query}",0.1)
            pyautogui.press('enter')   

        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt','d')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}",0.1)
            # pyautogui.press('tab')
            pyautogui.press('enter')
            
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')

        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')   

        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')

        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl' ,'j')

        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')

        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')

        elif 'close chrome' in query:
            os.system("taskkill/f /im chrome.exe") 

        elif 'close browser' in query:
            os.system("taskkill/f /im msEdge.exe") 

        elif 'jarvis' in query:
            print('Yes sir')
            speak('Yes Sir')   
    
        elif 'volume up' in query:
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 
            pyautogui.press("volumeup") 

        elif 'volume down' in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif 'mute' or 'unmute' in query:
            pyautogui.press("volumemute")    

        elif "end"or"exit"or"stop"or"quit" in query:
            exit()           
