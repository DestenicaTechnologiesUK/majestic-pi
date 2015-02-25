from Tkinter import *

from PIL import Image, ImageTk

import ttk

import os



root = Tk()

def change1():

	v.set("Setting Dimensions...")


def change2():
	v.set("Mounting MajesticPi To Raspberry Pi...")


def change3():

	v.set("Loading...")

def load():

	root.destroy()
	os.system("python cinema.py")

if __name__ == '__main__':

	v = StringVar()


	img = Image.open('splash.jpg')
	image = ImageTk.PhotoImage(img)

	Label(root, image=image).pack()

	v.set("Initialising MajesticPi...")

	root.overrideredirect(True)

	progressbar = ttk.Progressbar(orient=HORIZONTAL, length=1000, mode='determinate')
	progressbar.pack(side="bottom")
	progressbar.start()
	Label(root, textvariable=v).pack()

	root.after(2000, change1)
	root.after(4000, change2)
	root.after(6000, change3)

	root.after(10000, load)
	root.mainloop()
