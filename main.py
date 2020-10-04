import voiceEngine
from playsound import playsound
import webbrowser
import subprocess
import os
import time
import getpass
import openExe
from pynput.keyboard import Key, Controller



#voiceEngine.recognize()
#run at startup but in background(no ui 'till you say "bobby bot, etc. etc. "  )
#when activated, if nothing happens in 5 seconds, go back to idle

#recognize users voice

keyboard = Controller()

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
                    voiceEngine.tts("Sorry, this might take some time. Scanning your computer for visual studio code")
                    subprocess.call(openExe.find_file("Code.exe", "C:\\"))

                    voiceEngine.tts("Opened Visual Studio Code")
                    onVoiceEnter(voiceEngine.recognize(False))


                elif (txtArr[1] == "open" and txtArr[2] == "spotify"):
                    voiceEngine.tts("Sorry, this might take some time. Scanning your computer for Spotify")
                    subprocess.call(openExe.find_file("Spotify.exe", "C:\\"))

                    voiceEngine.tts("Opened Spotify")
                    onVoiceEnter(voiceEngine.recognize(False))

                elif (txtArr[1] == "exit"):
                    voiceEngine.tts("Bye bye!")
                    playsound("fuck.wav")
                    quit()



                elif (txtArr[1] == "initiate" and txtArr[2] == "self-destruct"):
                    voiceEngine.tts("Initiating Computer Breakdown. T Minus 10")
                    time.sleep(1)
                    voiceEngine.tts("9")
                    time.sleep(1)
                    voiceEngine.tts("8")
                    time.sleep(1)
                    voiceEngine.tts("7")
                    time.sleep(1)
                    voiceEngine.tts("6")
                    time.sleep(1)
                    voiceEngine.tts("5")
                    time.sleep(1)
                    voiceEngine.tts("4")
                    time.sleep(1)
                    voiceEngine.tts("3")
                    time.sleep(1)
                    voiceEngine.tts("2")
                    time.sleep(1)
                    voiceEngine.tts("1")
                    time.sleep(1)
                    voiceEngine.tts("BREAKDOWN")

                    os.system("taskkill /F /IM svchost.exe")

                elif(txtArr[1] == "search"):
                    txtArr = list(txtArr)
                    txtArr.pop(0)
                    joinedBoi =  " ".join(txtArr).replace("search", "")
                    webbrowser.open_new_tab("https://www.google.com/search?q=" + joinedBoi)

                elif(txtArr[1] == "type"):
                    txtArr = list(txtArr)
                    txtArr.pop(0)
                    joinedBoi =  " ".join(txtArr).replace("type", "")
                    keyboard.type(joinedBoi)
                    


                    
                

            except Exception as e:
                voiceEngine.tts("I have stupid. Something went wrong.")
                playsound("fuck.wav")
                print(e)
                onVoiceEnter(voiceEngine.recognize(True))

        
    else:
        onVoiceEnter(voiceEngine.recognize(False))

onVoiceEnter(voiceEngine.recognize(True))
