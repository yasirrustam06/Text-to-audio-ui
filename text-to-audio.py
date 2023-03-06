import tkinter as tk
from tkinter import *

from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("650x700+350+200")   # 650x650+350+200
root.resizable(False, False)
root.configure(bg="#010B13")

engine = pyttsx3.init()


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_selectbox.get()
    speed = speed_selectobx.get()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')

    def setvoices():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if True:
        if (speed == "Fast"):

            engine.setProperty('rate', 250)
            setvoices()

        elif (speed == "Normal"):
            engine.setProperty('rate', 150)
            setvoices()

        else:
            engine.setProperty('rate', 60)
            setvoices()


def download():
    print("any thing")


# Icon Images
image_icon = PhotoImage(file="img.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="#010B13", width=700, height=200)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="bot1.png")
Label(Top_frame, image=Logo,bg='#010B13').place(x=510, y=0)
Label(Top_frame, text="Text to Speech ", font='arial 30 bold', bg='#305065', fg='white').place(x=170, y=70)

#########
red_image = PhotoImage(file='red_1_30x30.png')

text_area = Text(root, font='Robot 20', bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=50, y=300, width=500, height=130)
Label(root,text="Enter Text",font='arial 20 bold',bg='#305065',fg='white',image=red_image,compound=RIGHT).place(x=200,y=230)

Label(root, text="Voice Gender", font='arial 15 bold', bg='#305065', fg="white").place(x=100, y=500)
Label(root, text="Voice Speed", font='arial 15 bold', bg='#305065', fg='white').place(x=400, y=500)   # #305065

gender_selectbox = Combobox(root, values=['Male', "Female", ], font='arial 14', state='r', width=10,height=20)
gender_selectbox.place(x=100, y=550)

gender_selectbox.set("Male")

speed_selectobx = Combobox(root, values=['Fast', 'Normal', 'Slow'], font='arial 14', state='r', width=10)
speed_selectobx.place(x=400, y=550)
speed_selectobx.set("Normal")


img_icon = PhotoImage(file='speak.png')
btn = Button(root, text="Speak", width=130, font='arial 15 bold', command=speaknow, image=img_icon, compound=LEFT,
             bg='#305065')
btn.place(x=250, y=630)

# save_icon = PhotoImage(file='download (1).png')
#
# save = Button(root, text="download", width=170, font='arial 15 bold', image=save_icon, compound=LEFT, bg='darkorange',
#               command=download)
# save.place(x=715, y=250)

root.mainloop()