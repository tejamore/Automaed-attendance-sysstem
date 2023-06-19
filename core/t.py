import pyttsx3
 import random

 engine = pyttsx3.init()
 words = ['hello', 'word']     
 engine.say(random.choice(words))
 newVoiceRate = 145
 engine.setProperty('rate',newVoiceRate)