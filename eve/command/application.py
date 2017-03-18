#Program to generate application
import textwrap

#outputFile = "file1.txt"

class Application():
    """docstring for application"""

    def readValue(self):
        self.sender = raw_input("Sender: ")
        self.sender=self.sender[0].upper()+self.sender[1:]

        self.reciever = raw_input("Reciver: ")
        self.reciever=self.reciever[0].upper()+self.reciever[1:]

        self.subject = raw_input("Subject: ")
        self.subject=self.subject[0].upper()+self.subject[1:]

        self.body = raw_input("Body: ")
        self.body=self.body[0].upper()+self.body[1:]

        self.outputFile = raw_input("File name: ")
        

    def generateApplication(self):
        fo = open(outputFile,"w")
        fo.write("To,")
        fo.write("\n\t"+self.reciever)
        fo.write("\n")
        fo.write("\nSubject: "+self.subject+"\n")
        fo.write("\nSir/Maam,")
        fo.write("\n\t")
        fo.close()
        with open(self.outputFile, "a") as fo:
            fo.write(textwrap.fill(self.body, width=90))
        fo.close()

        fo = open(outputFile,"a")    
        fo.write("\n\nThank You")
        fo.write("\nYour sincerly,")
        fo.write("\n"+self.sender)
        fo.close()

def main():
    a = Application()
    a.readValue()
    a.generateApplication()

if __name__ == '__main__':
    main()