import pyttsx3
import speech_recognition as sr
from playsound import playsound

engine = pyttsx3.init()
r = sr.Recognizer()



#create function for tts
def tts(whatsay):
    if type(whatsay) == str:
        engine.setProperty("rate", 140)
        engine.say(whatsay)

        
        
        engine.runAndWait()


        #engine.runAndWait()
    else:
        print("Error. Input is not str")

wakeword = "barbie"

def recognize():
    with sr.Microphone() as source:
        tts("At your service. To wake me up, say bobby")
        playsound("readysound.wav")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language="en-US")
            txtArr = text.lower().split()
            return txtArr

            
        except:
            tts("Sorry. Didn't catch that. I have stupid.")
            return ""
    