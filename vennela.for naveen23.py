import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

listener = sr.Recognizer()
def speak(cmd):
    tts = gTTS(cmd, lang='te')
    tts.save('audio.mp3')
    playsound('audio.mp3')
    os.remove('audio.mp3')

gf_name='అమృత'

speak("హాయ్ నేను మీ అమృతను మీకు ఏదైనా సహాయం కావాలంటే చెప్పండి నేను చేస్తాను")

def tack_command():
    try:
        with sr.Microphone() as source:
            print("listening.......")
            listener.pause_threshold=1
            listener.energy_threshold=5000
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language="te")
            if gf_name in command:
                print(command)
                speak(command)
    except:
        print("check your mic")

while True:
    tack_command()