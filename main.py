import JarvisAI
import re
import pprint
import random
import webbrowser
import os
from time import sleep
import ybc_camera
import cv2,time
from datetime import datetime
import time
import playsound
import win10toast
obj = JarvisAI.JarvisAssistant()
ti = time.strftime('%H%M')
print(ti)
t = 0
def ala():
    m = int(input("Alarm"))
    e = int(input("Duration will be"))
    if m == ti:
     t = win10toast.ToastNotifier()
     t.show_toast("Simps", "you have to wake now", duration=e)
def t2s(text):
    obj.text2speech(text)
def add(text):
    obj.text2speech(text)
ala()
while True:
    res = obj.mic_input()

    if re.search('weather|temperature', res):
        city = res.split(' ')[-1]
        weather_res = obj.weather(city=city)
        print(weather_res)
        t2s(weather_res)

    if re.search('news', res):
        news_res = obj.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
        t2s(news_res[0])
        t2s(news_res[1])

    if re.search("rock", res):
        choice = ['rock','paper','scicssors']
        t2s("REady to play. rOCK PAPER SCISSORS WITH ME")
        add(choice[random.randrange(0,2,+1)])
        print(choice[random.randrange(0, 2, +1)])

    if re.search('tell me about', res):
        topic = res.split(' ')[-1]
        wiki_res = obj.tell_me(topic)
        print(wiki_res)
        t2s(wiki_res)


    if re.search('time', res):
        time = obj.tell_me_time()
        print(time)
        t2s(time)
        d = input("do you want date also input d if you want")
        t2s("do you want date also  if you want")
        dae = obj.mic_input()
        if re.search('d', add):
            date = obj.tell_me_date()
            print(date)
            print(t2s(date))


    if re.search('open', res):
        domain = res.split(' ')[-1]
        open_result = obj.website_opener(domain)
        sleep(15)
        print(open_result)

    if re.search('launch', res):
        dict_app = {
            'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe',
            'age': 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'}
        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application path not found')
            print('Application path not found')
        else:
            t2s('Launching: ' + app)
            obj.launch_any_app(path_of_app=path)

    if re.search("football",res):
        site = ["dailymaily.com","skysport.com","espn.com"]
        webbrowser.open_new_tab(site[random.randrange(0,2,+1)])
        t2s("of course boss. Boss i can help you by opening the website that you want")
        print(site[random.randrange(0,2,+1)])


    if re.search('hello', res):
        print('Hi')
        t2s('Hi')

    if re.search('how are you', res):
        li = ['I m felling good', 'i am feeling great', 'I am feeling nice']
        response = random.choice(li)
        print(f"I am {response}")
        t2s(f"I am {response}")

    if re.search('your name|who are you', res):
        print("My name is baby, I am your personal assistant")
        t2s("My name is baby, I am your personal assistant")
    if re.search('good bye',res):
        print('ok Goodbye')
        t2s("ok Goodbye")
        quit(t2s(),obj,JarvisAI)
    if re.search("take me",res):
        t2s("do you want to take a photo i am opening your webcam")
        print("wait few seconds")


    if re.search('what can you do', res):
        li_commands = {
            "open websites": "Example: 'open youtube.com",
            "time": "Example: 'what time it is?'",
            "date": "Example: 'what date it is?'",
            "launch applications": "Example: 'launch chrome'",
            "tell me": "Example: 'tell me about Ethiopia'",
            "weather": "Example: 'what weather/temperature in Addiss ababa?'",
            "news": "Example: 'news for today' ",

        }
        ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
        I can open websites for you, launch application and more. See the list of commands-"""
        print(ans)
        pprint.pprint(li_commands)
        t2s(ans)
