import time
import random
import pyttsx3

colors = ["赤", "青", "緑", "黄色", "空中"]
body_parts = ["右手", "右足", "左手", "左足"]
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def twister():
    random_color = random.choice(colors)
    random_body_part = random.choice(body_parts)
    return  f"{random_body_part} ,{random_color}"

while True:
    engine.say(twister())
    engine.runAndWait()
    time.sleep(5)
    
