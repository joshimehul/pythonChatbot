import os
import pyaudio
from gtts import gTTS
import speech_recognition as sr
import webbrowser
import smtplib
def talkToMe(audio):
    print(audio)
    take= gTTS(text = audio , lang = 'en')
    take.save('audio.mp3')
    os.system('audio.mp3')
#listens command
def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('i am ready for your command')
        r.pause_threshold =1
        r.adjust_for_ambient_noise(source,duration = 1)
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("you said:" + command+ "\n")

#loop back to continue to listen to the commands
        except sr.UnknownValueError:
            assistant(mycommand())
        return command
#if  statements for executing commands
def assistant(command):
    if 'hello' in command:
        talkToMe('hello mehul')
    if 'open unity' in command:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = 'https://www.youtube.com/'
        webbrowser.get(chrome_path).open(url)
    if 'what\'s up' in command:
        talkToMe('chilling dude')
    if 'email' in command:
        talkToMe('who is the recipent')
        recipent = mycommand()
        if 'mahadev' is recipent:
            talkToMe('what should i say')
            content = mycommand()
            #init gmail smtp
            mail = smtplib.SMTP('smtp.gmail.com',587)
            #identity to server
            mail.ehlo()
            #encrypt session
            mail.starttls()
            #login
            mail.login('mehul joshi','bentleymalshan')
            #send message
            mail.sendmail('person name','joshimehul005@gmail.com',content)
            #close connection
            mail.close()
            talkToMe('Email sent')
    talkToMe('im ready for your command')
while True:
    assistant(mycommand())