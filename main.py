import voiceEngine
from playsound import playsound
import webbrowser
import subprocess
import os
import time
import getpass
import openExe
import multiprocessing
from pynput.keyboard import Key, Controller
import server


if __name__ == '__main__':
    ServerProcess = multiprocessing.Process(target=server.run)
    ServerProcess.start()
    webbrowser.open_new_tab("http://localhost:5500")
    






def SimonSays(txtArr):
    txtArr = list(txtArr)
    txtArr.pop(0)
    joinedBoi =  " ".join(txtArr).replace("simon", "").replace("says", "")
    voiceEngine.tts(joinedBoi)
    onVoiceEnter(voiceEngine.recognize(False))
    






def OpenBrowser():
    webbrowser.open("https://www.google.com")
    voiceEngine.tts("Opened browser successfully")
    onVoiceEnter(voiceEngine.recognize(False))
    


def OpenVSCode():
    voiceEngine.tts("Sorry, this might take some time. Scanning your computer for visual studio code")
    subprocess.call(openExe.find_file("Code.exe", "C:\\"))
    voiceEngine.tts("Opened Visual Studio Code")
    onVoiceEnter(voiceEngine.recognize(False))


def OpenSpotify():
    voiceEngine.tts("Sorry, this might take some time. Scanning your computer for Spotify")
    subprocess.call(openExe.find_file("Spotify.exe", "C:\\"))

    voiceEngine.tts("Opened Spotify")
    onVoiceEnter(voiceEngine.recognize(False))



def SelfDestruct():
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

def ExitProg():
    voiceEngine.tts("Bye bye!")
    playsound("fuck.wav")
    quit()

def Search(txtArr):
    txtArr = list(txtArr)
    txtArr.pop(0)
    joinedBoi =  " ".join(txtArr).replace("search", "")
    webbrowser.open_new_tab("https://www.google.com/search?q=" + joinedBoi)
    onVoiceEnter(voiceEngine.recognize(False))


def Type(txtArr):
    txtArr = list(txtArr)
    txtArr.pop(0)
    joinedBoi =  " ".join(txtArr).replace("type", "")
    keyboard.type(joinedBoi)
    onVoiceEnter(voiceEngine.recognize(False))

def OpenMenu():
    webbrowser.open_new_tab("http://localhost:5500/")


OpenMenu()






keyboard = Controller()

def init():
    pass

def onVoiceEnter(txtArr):
    if (txtArr != []):
        if txtArr[0] in voiceEngine.wakewords:


            playsound("sounds/readysound.wav")
            try:

                #simon says func
                if(txtArr[1] == "simon" and txtArr[2] == "says"):
                    SimonSays(txtArr)
 
                    
                
                #open google func
                elif (txtArr[1] == "open" and txtArr[2] == "browser"):
                    OpenBrowser()
                  


                
                #Open VSCODE function
                elif (txtArr[1] == "open" and txtArr[2] == "visual" and txtArr[3] == "studio" and txtArr[4] == "code"):
                    OpenVSCode()


                elif (txtArr[1] == "open" and txtArr[2] == "spotify"):
                    OpenSpotify

                elif (txtArr[1] == "exit"):
                    ExitProg()




                elif (txtArr[1] == "initiate" and txtArr[2] == "self-destruct"):
                    SelfDistruct()
                    

                elif(txtArr[1] == "search"):
                    Search(txtArr)


                elif(txtArr[1] == "type"):
                    Type(txtArr)

                elif(txtArr[1] == "open" and txtArr[2] == "menu"):
                    OpenMenu()

                else:
                	voiceEngine.tts("Sorry, I didn't catch that.")


                    
                

            except Exception as e:
                pass


        
    else:
        onVoiceEnter(voiceEngine.recognize(False))

onVoiceEnter(voiceEngine.recognize(False))
