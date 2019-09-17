from guizero import App, Text, TextBox, PushButton, Slider, Picture, Window

import tkinter as tk
import serial
import time
import os


arduino = serial.Serial("COM8",9600)




def select_3():
        flag3 = 0
        if flag3 == 0 :
            #os.system('notepad /p C:\\Users\\mahmo\\OneDrive\\Desktop\\3.txt')
            time.sleep(0.1) 
            arduino.write(b'3')
            os.system('notepad /p 3.txt')

            flag3 = 1
        return
  
def select_5():
        flag5 = 0
        if flag5 == 0 :
            time.sleep(0.1) 
            arduino.write(b'5')
            os.system('notepad /p 5.txt')
            flag5 = 1
        return


def select_7():
        flag7 = 0
        if flag7 == 0 :
            time.sleep(0.1) 
            arduino.write(b'7')    
            os.system('notepad /p 7.txt')
            flag7 = 1
        return
    
def select_10():
        
        flag10 = 0
        if flag10 == 0 :
            time.sleep(0.1) 
            arduino.write(b'9')
            os.system('notepad /p ten.txt')
            flag10 = 1
        return 


def open_window():
    window.show()

def close_window():
    window.hide()
 
    
app = App(title="مترو")
    #app = App(layout="grid")


window = Window(app, title="Map")
window.hide()



maintext = Text(app, text="نوع التذكره"
                        ,size=60
                        ,font="Times new roman"
                        ,color="red")

open_button = PushButton(app, command=open_window ,pady=80, padx=150 , text="Show Map")

x_3= PushButton(app,command=select_3 ,pady=50, padx=120,text=" 3 جنيه",align="left")
x_5 = PushButton(app,command=select_5 ,pady=50,padx=120,text=" 5 جنيه",align="left")
x_7 = PushButton(app,command=select_7 ,pady=50,padx=120,text=" 7 جنيه",align="left")
x_10= PushButton(app,command=select_10 ,pady=50, padx=120,text="10 جنيه",align="left")

close_button = PushButton(window, command=close_window ,pady=50, padx=100, text="Choose ticket" ,align="left")

picture = Picture(window,  width=700, height=950, image="map.png",align="right")



app.display()


