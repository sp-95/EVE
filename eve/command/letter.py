#Program to generate letter
import textwrap
import subprocess

#output_file = "letter.txt"

class Letter():
    """docstring for letter"""

    def read_value(self):
        self.sender = raw_input("Sender: ")
        self.sender=self.sender[0].upper()+self.sender[1:]

        self.reciever = raw_input("Reciver: ")
        self.reciever=self.reciever[0].upper()+self.reciever[1:]

        self.subject = raw_input("Subject: ")
        self.subject=self.subject[0].upper()+self.subject[1:]

        self.body = raw_input("Body: ")
        self.body=self.body[0].upper()+self.body[1:]

        self.output_file = raw_input("File name: ")

    def generate_letter(self):
        with open(self.output_file,"w") as f:
            f.write("To,")
            f.write("\n\t"+self.reciever)
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