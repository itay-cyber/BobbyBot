import voiceEngine
from playsound import playsound
import webbrowser



voiceEngine.tts("Hi.")


#voiceEngine.recognize()
#run at startup but in background(no ui 'till you say "bobby bot, etc. etc. "  )
#when activated, if nothing happens in 5 seconds, go back to idle

#recognize users voice




def init():
    pass

def onVoiceEnter(txtArr):
    if txtArr[0] == voiceEngine.wakeword:
        playsound("readysound.wav")
        try:
            #simon says func
            if(txtArr[1] == "simon" and txtArr[2] == "says"):
                voiceEngine.tts("simon says") 
                joinedBoi =  txtArr.join(" ").replace(voiceEngine.wakeword, "").replace("simon", "").replace("says", "")
                voiceEngine.tts(joinedBoi)
                
            
            #open google func
            elif (txtArr[1] == "open" txtArr[2] == "browser"):
                try:
                    webbrowser.open("https://www.google.com")
                    voiceEngine.tts("Opened browser successfully")
                except:
                    voiceEngine.tts("I have stupid. Something went wrong.")
                
                
            

        except:
            voiceEngine.tts("I have stupid. Something went wrong.")



onVoiceEnter(voiceEngine.recognize())
