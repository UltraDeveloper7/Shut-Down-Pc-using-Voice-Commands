import pyttsx3
import speech_recognition as sr
import os
import time

def TakeCommands():
    # Initialize speech_recognition
    speech_recognizer = sr.Recognizer()
    # Open physical microphone of your computer
    with sr.Microphone() as source_mic:
        print('Listening/Waiting.....')
        speech_recognizer.pause_threshold = 0.7
        # Store audio to audio variable
        audio_store = speech_recognizer.listen(source_mic)
        try:
            print("Recognizing...")
            # Recognize audio using google api
            Question = speech_recognizer.recognize_google(audio_store)
            print("You answered: {}". format(Question))
        except Exception as e:
            print(e)
            print("Say that again Mister")
            # Return 'None' if there are errors while you are speaking!
            return "None"
    # Return audio as text   
    time.sleep(2)
    return Question


# Create a function to implement the instructions of your voice through the voice assistant.
def Speak(audio_store):
    speaker = pyttsx3.init()
    speaker.say(audio_store)
    speaker.runAndWait()

Speak("Welcome back Mister what action would you like to perform for you")
Speak("For voice commands press 1 or for keyboard usage press 2")


if __name__ == '__main__':
    while True:    
        choice = input("Choice '1' or '2':")
        while choice == '1':
            Speak("Do you want to shutdown restart or hibernate your computer")
            command = TakeCommands()
            if "neither" in command:
                Speak("Thank you Mister I won't shut or restart down the computer")
                break
            if  "shutdown" or "shut down"  in command:
                Speak("I will Shut down the computer immediately!")
                os.system("shutdown /s /t 0")
                break
            if "restart" in command:
                Speak("I will restart the computer immediately!")
                os.system("shutdown /r /t 0")
                break
            if "hibernate" in command:
                Speak("I will hibernate the computer immediately!")
                os.system("shutdown.exe /h")
                break
            Speak("Say that again Mister")
        while choice == '2':
            choice2 = input("For shuting down the computer press (3).\nFor restarting the computer press (4).\nFor hibernating the computer press (5).\nChoice:")
            if choice2 == '3':
                os.system("shutdown /s /t 0")
                break
            if choice2 == '4':
                os.system("shutdown /r /t 0")
                break
            if choice2 == '5':
                os.system("shutdown.exe /h")
                break
            
        
