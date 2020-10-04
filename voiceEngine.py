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

wakewords = ["bobby", "barbie", "barbie's", "bobby's"]


def recognize(issound):
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=1)
        if (issound == True):
            playsound("readysound.wav")
        else:
            pass
        
        audio = r.listen(source)

        text = r.recognize_google(audio, language="en-US")
        try:
            txtArr = str(text).lower().split()
        except:
            pass


        if (txtArr != []):
            print(txtArr)
            return txtArr
        else:
            return
