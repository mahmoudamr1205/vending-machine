from guizero import App, Text, TextBox, PushButton, Slider, Picture, Window

import tkinter as tk


#import RPi.GPIO as GPIO

# arabic or english

def select_3():
    print("ابو 3")
    return
  
def select_5():
    print(" واحده من ابو  5")
    return


def select_7():
    print(" ابو 7")
    return
    
def select_10():
    print("ابو 10 و هات الباقى")
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

open_button = PushButton(app, command=open_window ,pady=50, padx=100 , text="Show Map")

x_3= PushButton(app,command=select_3 ,pady=50, padx=100,text=" 3 جنيه",align="left")
x_5 = PushButton(app,command=select_5 ,pady=50,padx=100,text=" 5 جنيه",align="left")
x_7 = PushButton(app,command=select_7 ,pady=50,padx=100,text=" 7 جنيه",align="left")
x_10= PushButton(app,command=select_10 ,pady=50, padx=100,text="10 جنيه",align="left")

close_button = PushButton(window, command=close_window ,pady=50, padx=100, text="Choose ticket" ,align="left")

picture = Picture(window,  width=700, height=950, image="map.png",align="right")





app.display()
