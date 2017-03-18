#Program to generate letter
import textwrap
import subprocess
import speech_recognition as sr

import note

#output_file = "letter.txt"

class Letter():
    """docstring for letter"""
    def read_value(self):
        subprocess.call(['say', 'Who is the sender?'])
        self.sender = raw_input("Enter sender: ").capitalize()

        subprocess.call(['say', 'Who is the receiver?'])
        self.receiver = raw_input("Enter receiver: ").capitalize()

        subprocess.call(['say', 'What is the subject?'])
        self.subject = raw_input("Enter the subject: ").capitalize()

        subprocess.call(['say', 'Tell me what to write'])
        self.body = note.main().capitalize()

        subprocess.call(['say', 'Saving the file as letter dot txt'])
        self.output_file = 'letter.txt'

    def generate_letter(self):
        with open(self.output_file,"w") as f:
            f.write("To,")
            f.write("\n\t"+self.receiver)
            f.write("\n")
            f.write("\nSubject: "+self.subject+"\n")
            f.write("\nSir/Maam,")
            f.write("\n\t")

            f.write(textwrap.fill(self.body, width=90))

            f.write("\n\nThank You")
            f.write("\nYour sincerly,")
            f.write("\n"+self.sender)

        subprocess.call(['open', self.output_file])
        return self.output_file

def main():
    a = Letter()
    a.read_value()
    return a.generate_letter()

if __name__ == '__main__':
    main()