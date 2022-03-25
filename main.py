import time
import winsound
import threading
from datetime import datetime
#-----------------------------------#
#This section is meant to display the time. I have it checking to see if countdown is still alive and if it is, then it'll do something. I honestly can't remember what tf I was thinking when I started that, but that is how it is for now. I'll probably go ahead and change it later cause looking back at it after not for a few days, that shit looks wack.
def display_time():
    
    global thread_countdown
    while True:
        try:
            if thread_countdown.is_alive:
                pass #add something else here
            else:
                print(datetime.now().strftime("%H:%M:%S"))
                time.sleep(1)
        except:
            print(datetime.now().strftime("%H:%M:%S"))
            time.sleep(1)
#-----------------------------------#
def countdown(seconds):
    while seconds >= 0:
        print(datetime.now().strftime("%H:%M:%S"))
        seconds -= 1
        time.sleep(1)
    print("Done")
    #winsound.Beep(3000, 1000)
#-----------------------------------#
class alarm_clock():
    def __init__(self):
        print(datetime.now().strftime("%H:%M:%S"))
        self.time_set()
    
    def time_set(self):
        self.seconds = int(input("How many seconds: "))
    #This run method honestly looks terrible. I hate it. But this was like the messy and brute way I got things to display.Pretty sure the try and except stuff can be removed and this run method can be cut down a lot and the work can be put in other methods most likely.
    def run(self):
        if self.seconds <= -1:
            quit()
        else:
            while self.seconds >= 0:
                thread_countdown = threading.Thread(target=countdown, args=(self.seconds,))
                thread_countdown.start()
                thread_countdown.join()
                try:
                    if not thread_display.is_alive:
                        thread_display.start()
                except:
                    thread_display = threading.Thread(target=display_time)
                    thread_display.start()
                self.time_set()
                if self.seconds <= -1:
                    quit()

#-----------------------------------#
if __name__ == "__main__":
    test = alarm_clock()
    test.run()
#-----------------------------------#

#This section below is just the original. It can be ignored overall.

#def countdown(seconds):
    #while seconds:
    #    time.sleep(1)
   #     seconds -=1
  #  winsound.Beep(3000, 1000)
 #   print("Done")

#def get_user_input_time():
   # time = int(input("Enter seconds before alarm: "))
   # return time


#if __name__ == "__main__":
 #   input_time = get_user_input_time()
  #  countdown(input_time)