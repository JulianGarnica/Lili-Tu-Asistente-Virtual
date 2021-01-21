
import urllib.parse
import requests
from playsound import playsound
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec malesuada, elit sed accumsan pretium, mauris augue faucibus nibh, a lacinia elit turpis sed est."
texto = urllib.parse.quote(texto)

url = r"https://translate.google.com.co/translate_tts?ie=UTF-8&q="+texto+r"&tl=es&client=tw-ob"

myfile = requests.get(url)

open('test.mp3', 'wb').write(myfile.content)


playsound("test.mp3")
"""
https://translate.google.com.co/translate_tts?ie=UTF-8&q=Hola Julián! Qué te gustaría hacer hoy?&tl=es&client=tw-ob.mpeg
from datetime import date
import sched, time 
s = sched.scheduler(time.time, time.sleep) 
def do_something(sc): 
    today = date.today()
    current_time=today
    print (current_time)
    # do your stuff 
    s.enter(10, 1, do_something, (sc,)) 

s.enter(10, 1, do_something, (s,)) 
s.run() 

"""
