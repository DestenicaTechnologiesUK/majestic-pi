import os,sys,time
import time

def RunPlaylist():
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
        RunPlaylist()
