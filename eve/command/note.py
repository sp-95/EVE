#!/usr/bin/env python


import subprocess
import speech_recognition as sr


def main(save=False):
    """Main entry points
    """
    if save:
        subprocess.call(['say', 'Please tell me what to write'])
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            message = r.recognize_google(audio)
            punctuations = {
                            '.': [' period', ' full stop', ' fullstop'],
                            '?': [' question mark'],
                            ',': [' comma'],
                            '!': [' exclamation mark'],
                            ':': [' colon'],
                            ';': [' semicolon'],
                            '"': ['double quote', 'double quotes'],
                            '-': [' hyphen ', ' dash '],
                            '_': [' underscore '],
                            '(': ['opening bracket ', 'bracket open '],
                            ')': [' closing bracket', ' bracket close']
                            }
            for k, v in punctuations.items():
                for x in v:
                    message = message.replace(x, k)
            # print("You said " + message)
            if save:
                with open('note.txt', 'w') as f:
                    f.write(message)
            return message
        except sr.UnknownValueError:
            message = "I am sorry, could you repeat that for me?"
        except sr.RequestError:
            message = "Please check your internet connection"
        except:
            message = "Oh no! That was unexpected"
        subprocess.call(['say', message])


if __name__ == "__main__":
    main()
