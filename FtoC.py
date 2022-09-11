#Calculator Fharenheit to Celsius and Celsius to Fharenheit
#CH0L0H4TWH1T3
 
import tkinter
from tkinter import Label


def convert_to_celsius():
    fahrenheit = float(input_box.get())
    celsius = (fahrenheit * 9 / 5) + 32
    output_label.config(text=round(celsius, 2))

def fahrenheit_celsius(): 
    temp = float(input_box.get())
    f = float((float(temp -32)*5/9)) 
    Label(text ="%.1f Fahrenheit" % f) 
    output_label.config(text=round(f, 2))


window = tkinter.Tk()
window.title("Convertidor")
window.minsize(width=250, height=100)

input_box = tkinter.Entry()
output_label = tkinter.Label(text="", justify=tkinter.RIGHT, width=8)
action_button = tkinter.Button(text='        C°        ', command=convert_to_celsius)
action_butto = tkinter.Button(text='        F°        ', command=fahrenheit_celsius)
input_box.pack()
action_button.pack()
action_butto.pack()
output_label.pack()

window.mainloop()

