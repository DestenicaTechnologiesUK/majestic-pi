from Tkinter import *
from PIL import Image, ImageTk
import tkFileDialog
from __main__ import *
import os,sys

def reset():
	os.remove("current.txt")
	sys.exit()

master = Tk()
master.title("DCM - Home Cinema")
top = Label(master, text="Cinema!", font=("Helvetica", 50))
top.grid()
def adverts():
    global advertselector
    advertselector = tkFileDialog.askopenfilename(filetypes = (("Digital Cinema Advertising Package", "*.dca.mp4"),("All files", "*.*") ))
def hdmi():
    master.destroy()
    c = open('current.txt', 'a')
    c.close()
    w = open('current.txt', 'w')
    w.write('/home/pi/Desktop/majestic-pi/' + dim.get() + '/intro.mp4\r\n')
    w.write('/home/pi/Desktop/majestic-pi/' + dim.get() + '/glasses.mp4\r\n')
    w.write('/home/pi/Desktop/majestic-pi/' + dim.get() + '/mimics/' + cinema.get() + '/1.mp4\r\n')
    w.write(dcp.get() + 'trailer.mp4' + '\r\n')
    w.write('/home/pi/Desktop/majestic-pi/' + dim.get() + '/mimics/' + cinema.get() + '/2.mp4\r\n')
    w.write(advertselector + '\r\n')
    w.write('/home/pi/Desktop/majestic-pi/' + dim.get() + '/mimics/' + cinema.get() + '/3.mp4\r\n')
    w.write('/home/pi/Desktop/majestic-pi/' + dim.get() + '/mimics/' + cinema.get() + '/soundintro.mp4\r\n')
    w.write(dcp.get() + 'filmintro.mp4' + '\r\n')
    w.write(dcp.get() + 'film.mp4' + '\r\n')
    w.write('/home/pi/Desktop/majestic-pi/' + dim.get() + '/mimics/' + cinema.get() + '/4.mp4\r\n')
    w.close()
    os.system("python prepare.py & sudo python play.py")

dcp = StringVar(master)
dcp.set("Choose")

drivelabel = Label(master, text="Select DCP:")
drive = OptionMenu(master, dcp, "C:/", "F:/", "G:/", "D:/")
drivelabel.grid(row=1)
drive.grid(row=1, column=1)

advertlabel = Label(master, text="Select Advert Package:")
advertbutton = Button(master, text="Browse", command=adverts)
advertlabel.grid(row=2)
advertbutton.grid(row=2, column=1)

cinema = StringVar(master)
cinema.set("Choose")
cinemalabel = Label(master, text="Choose Cinema Mimic:")
pick = OptionMenu(master, cinema, "Odeon", "Vue", "Cineworld")
cinemalabel.grid(row=4)
pick.grid(row=4, column=1)

dim = StringVar(master)
dim.set("Choose")

drivelabel = Label(master, text="Enable 3D:")
drive = OptionMenu(master, dim, "3D", "2D")
drivelabel.grid(row=5)
drive.grid(row=5, column=1)

img = Image.open("go.png")
go = ImageTk.PhotoImage(img)
label = Button(master, image=go, command=hdmi)
label.grid()

mainloop()

    
