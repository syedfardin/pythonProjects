from win32com.client import Dispatch
import speech_recognition as sr
import webbrowser

import wikipedia
import os
import random

global positive_reply_array
global thanking_reply_array
positive_reply_array = ["Ok Sir", "Sure Sir", "Alright sir"]  
thanking_reply_array = ["My pleasure sir", "thank you sir", "my duty sir"]

def tell(str):
    text = Dispatch (('SAPI.SpVoice'))
    text.speak(str)

r = sr.Recognizer()
def takeCommand():
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognising...')    
        query = r.recognize_google(audio, language = 'en-in')
        print(f'User said: {query}\n')


    except Exception as e:
        print(e)    
        print("Say that again please..")    
        return "None"

    return query

tell('welcome sir, how can I help you?')
while True:
    query = takeCommand().lower()

    if "wikipedia" in query:
        #tell("Searching wikipedia")
        query = query.replace("wikipedia", "")
        tell(f'searching wikipedia for {query}')
        results = wikipedia.summary(query, sentences=1)
        tell("according to wikipedia,")
        tell(results)

    elif query == "ok":
        tell(random.choice(thanking_reply_array))
        exit() 

    elif "sleep" in query:
           
        tell(random.choice(positive_reply_array))    
        exit()

    elif "open" and "image" in query:
        tell("sure sir, opening image glass")
        path = "C:\Program Files\ImageGlass\ImageGlass.exe"
        os.startfile(path)    

    elif "open python work directory" in query:
        tell("sure sir")
        path2 = "C:\\Users\\admin\Desktop\\Python projects"
        os.startfile(path2)

    elif "play" and "music" in query:
        tell("Playing right away sir")

        num = random.randint(1,7)
        path3 = f"C:\\Users\\admin\\Desktop\\Python projects\\jarvis project\\music\\{num}.mp3"
        os.startfile(path3)

    elif "chrome" in query:
        tell("opening chrome")    
        path = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
        os.startfile(path)

    elif "command prompt" in query:
        tell("opening command prompt")    
        os.system("start cmd")




    elif "open" and "sublime text" in query:
        tell("Sure sir.")
        path5 = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(path5)

    elif "code" in query:
        tell('Do you want me to open vs code or sublime sir?')
        while True:
            query = takeCommand().lower()
            if "code" in query:
                tell("opening VS code")
                path = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
                exit()


            elif "sublime" in query:
                tell('opening sublime text') 
                path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                os.startfile(path)
                exit() 

            elif "sleep" in query:
                tell("Going to sleep")      
                exit()

            else:
                exit()    



    elif "open" and "code" in query:
        tell("OK sir, opening Visual studio code")
        path6 = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path6)    
        exit()

    elif "introduce" in query:
        tell("I am Jarvis, Fardin's personal assistant. I cannot do much things, but yeah, I can help you.")


    elif "search on google" in query:
        tell("Ok sir, What do you want me to search for?")
        cm = takeCommand().lower()
        stream = "https://www.google.com/search?q="
        stream2 = cm.replace(" ", "+")
        mainStream = stream+stream2
        webbrowser.open(mainStream)

    elif "web development" in query:
        tell("Sir, do you want me to open code with harry?")
        cm = takeCommand().lower()    
        if "yes" in cm:
            tell(random.choice(positive_reply_array)+" opening code with harry web development playlist")
            webbrowser.open("https://www.youtube.com/playlist?list=PLu0W_9lII9agiCUZYRsvtGTXdxkzPyItg")

    elif "search" and "youtube" in query:
        tell("What do you want me to search sir?")      
        cm = takeCommand().lower()
        replace = cm.replace(" ", "+")
        final = "https://www.youtube.com/results?search_query="+replace
        #print(final)
        tell(f"Do you want me to search for{cm}")
        confirm = takeCommand().lower()

        if "yes" in confirm:
            tell("Alright sir, searching.")
            webbrowser.open(final)
            quit()

        if "no" in confirm:
            tell("Alright sir")    
            quit()

 

    elif "filmora" in query:
        tell('opening filmora 9')    
        path = "C:\Program Files\Wondershare\Filmora9\Wondershare Filmora9.exe"
        os.startfile(path)
        quit()


    elif "screenshots" in query:
        tell(" opening screenshots folder.")  
        os.startfile("C:\\Users\\admin\\Pictures\\Screenshots")
        quit()
        
    elif "open" and "far cry" in query:
        tell("Opening far cry, enjoy gaming sir,")
        os.startfile("E:\\Far Cry 2 Game\\Far Cry 2 real game\\bin\\farcry2")
        quit()    
        

    elif "webex"in query:
        tell('opening Cisco Webex Meet')    
        path = "C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe"
        os.startfile(path)
        
    elif "minecraft" in query:
        tell("opening Tlauncher minecraft, enjoy gaming sir.")    
        path = "C:\\Users\\admin\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
        os.startfile(path)

    elif "you are of no use" in query:
        tell("Sorry if i could not help you sir.")    

    else:
        tell("Do you want me to search it on google sir?")
        cm = takeCommand().lower()
        if "yes" in cm:
            tell("ok sir, searching for",query)
            stream1 = query.replace(" ", "+")
            mainStreamZ = "https://www.google.com/search?q="+stream1
            webbrowser.open(mainStreamZ)
            exit()

        if "no" in query:
            tell("OK sir.")    
            exit()

        else:
            exit()    


positive_reply_array = ["Ok Sir", "Sure Sir", "Alright sir"]        


