import speech_recognition as sr
import os

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
        '''print("Say that again please..")    
        return "None"
'''
    return query

while True:
    query = takeCommand().lower()
    if "wake up jarvis" in query:
        os.startfile("C:\\Users\\admin\\Desktop\\Python projects\\jarvis project\\main.py")