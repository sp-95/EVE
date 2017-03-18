#brightness control
import os

def brightControl(val):
	status = "connected"
	os.system('xrandr -q | grep \"connected\" > driver.txt')
	#LCD_driver = LCD_driver.split(' ')
	fi = open("driver.txt","r")
	LCD_driver = fi.read()
	#print "file content: "
	LCD_driver = LCD_driver.split(' ')[0]
	print LCD_driver
	cmd = "xrandr --output "+LCD_driver+" --brightness " +str(val)
	os.system(cmd)

def main():
	val = float(raw_input("Brightness % : "))
	brightness(val)

if __name__ == '__main__':
	main()
