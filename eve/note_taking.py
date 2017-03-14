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
            message = r.recognize_google(audio)
            punctuations = {
                            '.': [' period', ' full stop'],
                            '?': [' question mark'],
                            ',': [' comma'],
                            '!': [' exclamation mark'],
                            ':': [' colon'],
                            ';': [' semicolon'],
                            '"': ['double quote', 'double quotes'],
                            '-': [' hyphen ', ' dash ']
                            '_': [' underscore '],
                            '(': ['opening bracket ', 'bracket open '],
                            ')': [' closing bracket', ' bracket close']
                            }
            for k, v in punctuations.items():
                for x in v:
                    message = message.replace(x, k)
            print("You said " + message)
            with open('note.txt', 'w') as f:
                f.write(message)
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
