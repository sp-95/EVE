#!/usr/bin/env python


import subprocess
import speech_recognition as sr

# from eve import command, conversation

__author__ = "Shashanka Prajapati"


def main():
    """Main entry points
    """
    message = "I am EVE. How may I help you?"
    print(message)
    subprocess.call(['say', message])

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            print("You said " + r.recognize_google(audio))
            message = ""
        except sr.UnknownValueError:
            message = "I am sorry, could you repeat that for me?"
        except sr.RequestError:
            message = "Please check your internet connection"
        except:
            message = "Oh no! That was unexpected"
        print(message)
        subprocess.call(['say', message])


if __name__ == "__main__":
    main()
