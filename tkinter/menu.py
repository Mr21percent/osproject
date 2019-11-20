from tkinter import *
import 

window = Tk()

c1 = Canvas(window, bg = 'white', width = 300, height = 60)
c2 = Canvas(window, bg = 'white', width = 300, height = 60)

b1 = Button(window, text = '카드입력')
b2 = Button(window, text = '결제')

b1.grid(column = 3, row = 1)
b2.grid(column = 4, row = 1)

window.mainloop()
