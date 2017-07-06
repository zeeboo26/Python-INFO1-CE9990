""" This program creates a new flag """

import tkinter              

oldLightBlue  = '#87CEFA'
coolBlue = "#00559B"

stripeHeight = 35          #height of each stripe

#The root widget is the window that will contain everything we draw.
root = tkinter.Tk()
root.title("New flag")

#dimensions of entire flag, in pixels
height = 5 * stripeHeight  
width = int(height * 5/2) 
root.geometry(str(width) + "x" + str(height))
canvas = tkinter.Canvas(root)
canvas.pack()


def drawPixel(x, y, color):
    """
    Color the pixel at coordinates (x, y).
    """
    assert isinstance(x, int) and isinstance(y, int) and isinstance(color, str)
    canvas.create_rectangle(x, y, x + 1, y + 1, width = 0, fill = color)

y = 0
while y < height:
    x = 0
    while x < width:
        if y < stripeHeight or y > 4 * stripeHeight:
            drawPixel(x, y, oldLightBlue)                                       
        else:
            drawPixel(x, y, 'white')
        x += 1
    y += 1


y = 0
while y < height:
    x = 0
    while x < width:
        if (x < width * 5/16 or x > width * 7/16) and (y < 4 *  stripeHeight or y > 6 * stripeHeight):
            drawPixel(x, y, coolBlue)
        x += 1
    y += 1

canvas.create_oval(180, 70, 150, 100)

root.mainloop()
