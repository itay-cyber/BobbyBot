import voiceEngine
from playsound import playsound
import webbrowser
import subprocess
import os
import time


voiceEngine.tts("How are you doing milly!")


#voiceEngine.recognize()
#run at startup but in background(no ui 'till you say "bobby bot, etc. etc. "  )
#when activated, if nothing happens in 5 seconds, go back to idle

#recognize users voice

def init():
    pass

def onVoiceEnter(txtArr):
    if (txtArr != []):
        if txtArr[0] in voiceEngine.wakewords:
            playsound("readysound.wav")
            try:
                #simon says func
                if(txtArr[1] == "simon" and txtArr[2] == "says"):
                    txtArr = list(txtArr)
                    txtArr.pop(0)
                    joinedBoi =  " ".join(txtArr).replace("simon", "").replace("says", "")
                    voiceEngine.tts(joinedBoi)
                    onVoiceEnter(voiceEngine.recognize(False))
                    
                
                #open google func
                elif (txtArr[1] == "open" and txtArr[2] == "browser"):
                    webbrowser.open("https://www.google.com")
                    voiceEngine.tts("Opened browser successfully")
                    onVoiceEnter(voiceEngine.recognize(False))
                
                #Open VSCODE function
                elif (txtArr[1] == "open" and txtArr[2] == "visual" and txtArr[3] == "studio" and txtArr[4] == "code"):
                    subprocess.call("C:\\Users\\Itay G\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                    voiceEngine.tts("Opened Visual Studio Code")
                    onVoiceEnter(voiceEngine.recognize(False))
                elif (txtArr[1] == "exit"):
                    voiceEngine.tts("Bye bye!")
                    playsound("fuck.wav")
                    quit()
                elif (txtArr[1] == "initiate" and txtArr[2] == "self" and txtArr[3] == "destruct"):
                    voiceEngine.tts("Initiating Computer Breakdown. 10. 9. 8. 7. 6. 5. 4. 3. 2. 1. BREAKDOWN")
                    os.system("taskkill /F /IM svchost.exe")
                    
                

            except Exception as e:
                voiceEngine.tts("I have stupid. Something went wrong.")
                playsound("fuck.wav")
                print(e)
                onVoiceEnter(voiceEngine.recognize(True))
        else:
            print("no wakework said")
    else:
        onVoiceEnter(voiceEngine.recognize(False))

onVoiceEnter(voiceEngine.recognize(True))
