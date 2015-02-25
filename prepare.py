import os,sys,time

def SetScreensaver():
    for x in range(0,5): 
        os.system('xset -display :0.0 s 1 60 -dpms')
        time.sleep(60)
    return
                
if __name__ == '__main__':
    SetScreensaver()
    sys.exit()
