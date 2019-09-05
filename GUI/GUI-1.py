from guizero import App, Text, TextBox, PushButton, Slider, Picture

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



    
app = App(title="مترو")
#app = App(layout="grid")


maintext = Text(app, text="نوع التذكره"
                       ,size=60
                       ,font="Times new roman"
                       ,color="red")


x_3= PushButton(app,command=select_3 ,pady=40, padx=40,text=" 3 جنيه",align="left")
x_5 = PushButton(app,command=select_5 ,pady=40,padx=40,text=" 5 جنيه",align="left")
x_7 = PushButton(app,command=select_7 ,pady=40,padx=40,text=" 7 جنيه",align="left")
x_10= PushButton(app,command=select_10 ,pady=40, padx=40,text="10 جنيه",align="left")

picture = Picture(app,  width=700, height=950, image="map.png",align="right")


app.display()
