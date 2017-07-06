"""
This program creates lines to give an effect of perspective"
"""

import tkinter

root = tkinter.Tk()
root.title("Perspective")
canvas = tkinter.Canvas(root)
canvas.pack()


def drawLine(xStart, yStart, xEnd, yEnd, color):
    """
    Draw a straight line from point (xStart, yStart) to (xEnd, yEnd).
    """
    assert isinstance(xStart, int) and isinstance(yStart, int) and \
        isinstance(xEnd, int) and isinstance(yEnd, int) and \
        isinstance(color, str)

    canvas.create_line(xStart, yStart, xEnd, yEnd, width = 2, fill = color)

for i in range(25):
    drawLine(10 * i, 0, 70 * i, 400,"black")
   
for j in range (12):
        drawLine(0, 10 * j, 300, 10 * j, 'grey')
 
for i in range(8):
    drawLine(10 *i, 5* i, 50*i , 10*i, 'black')


             
root.mainloop()
