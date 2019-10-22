from tkinter import *
window = Tk()
canvas_1 = Canvas(window, bg = 'white', width = 700, height = 250)
canvas_2 = Canvas(window, bg = 'white', width = 400, height = 250)
canvas_3 = Canvas(window, bg = 'white', width = 300, height = 150)

canvas_1.grid(column = 1, row = 1, columnspan = 3)
canvas_2.grid(column = 3, row = 2, rowspan = 2)
canvas_3.grid(column = 1, row = 3, columnspan = 2)

b1 = Button(window, text = 'left')
b2 = Button(window, text = 'right')

b1.grid(column = 1, row =2)
b2.grid(column = 2, row =2)

window.mainloop()

