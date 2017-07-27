"""
gui.py

This program allow users to convert Farhenheit to Celsius by using a GUI
"""

from tkinter import*
def Temperature_conversion():
    temp = int((var.get() -32)* 5/9)
    convert = str(temp) + " Celsius"
    label2.config(text = convert)
root = Tk()
root.title("Temperature Converter")
root.resizable(0,0)

var = DoubleVar()

label1 = Label (root, text = "Temperature Converter\n Fahrenheit to Celsius",
                padx = 14, pady = 14, bd=14, fg ="Ivory", font =('arial',26,'bold'),
                bg ="navy blue", relief='raise',width = 20, height =3)

label1.pack()

slider = Scale(root, variable = var, from_= -50, to= 320, length = 450,
               orient = HORIZONTAL)

slider.pack(anchor = CENTER)

label2 = Label (root, padx = 14, pady = 14, bd=14, fg ="#000000", font =('arial',26,'bold'),
                bg ="Ivory", relief='sunk',
                width = 20, height =3)

label2.pack()

label3 = Label (root, text = " ")

label3.pack()
button = Button(root, text= "Go conversion", padx = 16, pady = 16, bd=16, width=10,
                 font =('arial',20,'italic'), command = Temperature_conversion)
button.pack(anchor= CENTER) #place button in the center
root.mainloop()
