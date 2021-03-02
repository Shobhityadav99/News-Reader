import json

import requests
r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=c4c10316899241c88721904ea2b93a3d")

data =r.json()
articles = data['articles']



def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
count = 1
if __name__ == '__main__':
    for items in articles:
        speak(f"Todays News are !"+ f"News no {count} is" +  items['title'])
        count = count + 1
        print(items['title'])