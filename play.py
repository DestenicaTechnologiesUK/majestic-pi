import os,sys,time
from Tkinter import *
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def RunPlaylist():
        hdmi.destroy()
        path    =    '/home/pi/Desktop/majestic-pi/current.txt' 
        file    =    open(path,'r')
        files   =    file.readlines()
        file.close()
        global cinema
        for file in files:
            filename = file.strip()
            if '.mp4' in filename:
                os.system('/usr/bin/omxplayer ' + filename)

if __name__ == '__main__':
    global hdmi
    hdmi = Tk()
    hdmi.title("DCM - Home Cinema")
    cable = Image.open("hdmi.png")
    cables = ImageTk.PhotoImage(cable)
    cableimage = Label(hdmi, image=cables)
    cableimage.grid()
    mainloop()
     
    while True:
            input_state = GPIO.input(8)
            if input_state == False:
                RunPlaylist()
                
