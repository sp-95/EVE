#!/usr/bin/env python


import subprocess
import speech_recognition as sr

from conversation import brain

__author__ = "Shashanka Prajapati"


def main():
    """Main entry points
    """
    message = "I am EVE. How may I help you?"
    print(message)
    subprocess.call(['say', message])

    r = sr.Recognizer()
    command = True
    active = True
    while active:
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                audio = r.recognize_google(audio)
                print("You said " + audio)
                if 'sleep' in audio:
                    active = False
                    message = "Goodbye! Hope to see you soon"
                elif command:
                    if(any(x in audio for x in ['command off', 'off command', 'dialogue', 'conversation'])):
                        command = False
                        brain.startup()
                        if('conversation' in audio):
                            message = "Switched to conversation mode"
                        else:
                            message = "Switched to dialogue mode"
                    else:
                        pass
                        message = ""
                else:
                    if(any(x in audio for x in ['command', 'dialogue off', 'conversation off', 'off dialogue', 'off conversation'])):
                        command = True
                        message = "Switched to command mode"
                    else:
                        message = brain.chat(audio)
            except sr.UnknownValueError:
                message = "I am sorry, could you repeat that for me?"
            except sr.RequestError:
                message = "Please check your internet connection"
            except Exception as e:
                message = "Oh no! That was unexpected"
                print(e)
            print(message)
            subprocess.call(['say', message])


if __name__ == "__main__":
    main()
