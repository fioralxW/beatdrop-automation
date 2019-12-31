
#Youtube music beat drop timing automation. By Fluzyx
#Inspired by the perfectly timing the crab rave drop by Ekhala on youtube.

"""PLEASE NOTE that the beat drop accuracy depends on your computer and
internet speed, so is recommended to adjust the seconds!"""

import datetime
import time
import webbrowser

def proc(h, m, s):
    while True:
        currentHour = datetime.datetime.now().hour
        currentMinute = datetime.datetime.now().minute
        currentSecond = datetime.datetime.now().second
        hour_left = (currentHour - h)
        min_left = (currentMinute - m) * -1
        sec_left = (currentSecond - s) * -1
        if currentHour >= h and currentMinute >= m and currentSecond >= s:
            print('\n')
            print("The magic happens!")
            webbrowser.open('https://www.youtube.com/watch?v=RR8NNoEXs00') #Youtube video url. can be a specific time
            break
        print("hour(s) left: " , hour_left)
        print("minute(s) left: " , min_left)
        print("second(s) left: ", sec_left)
        print('\n')
        time.sleep(1) #so that you wont get spammed
        
h = int(input("Enter the hour: "))  # 0-23
m = int(input("Enter the minute: ")) # 0-59
s = int(input("Enter the second (ADJUST FOR BEAT DROP ACCURACY!!!): ")) # 0-59

proc(h,m,s)
