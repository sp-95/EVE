#!/usr/bin/env python


import subprocess
import speech_recognition as sr
import random

import command.brain
import conversation.brain

__author__ = "Shashanka Prajapati"


def main():
    """Main entry points
    """
    message = "I am EVE. How may I help you?"
    print(message)
    subprocess.call(['say', message])

    helpStatements = ["Can I help you with something else?", "Is there something else you need?", "Anything else?", "Will that be all?"]

    r = sr.Recognizer()
    command_mode = True
    is_active = True
    while is_active:
        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                audio = r.recognize_google(audio)
                # print("You said " + audio)
                if 'sleep' in audio:
                    is_active = False
                    message = "Goodbye! Hope to see you soon"
                elif command_mode:
                    if(any(x in audio for x in ['command off', 'off command', 'dialogue', 'conversation'])):
                        command_mode = False
                        conversation.brain.startup()
                        if('conversation' in audio):
                            message = "Switched to conversation mode"
                        else:
                            message = "Switched to dialogue mode"
                    else:
                        message = command.brain.chat(audio)
                else:
                    if(any(x in audio for x in ['command', 'dialogue off', 'conversation off', 'off dialogue', 'off conversation'])):
                        command_mode = True
                        message = "Switched to command mode"
                    else:
                        message = conversation.brain.chat(audio)
            except sr.UnknownValueError:
                message = "I am sorry, could you repeat that for me?"
            except sr.RequestError:
                message = "Please check your internet connection"
            except Exception as e:
                message = "Oh no! That was unexpected"
                print(e)
            print(message)
            subprocess.call(['say', message])
            if is_active and command_mode:
                subprocess.call(['say', random.choice(helpStatements)])


if __name__ == "__main__":
    main()
