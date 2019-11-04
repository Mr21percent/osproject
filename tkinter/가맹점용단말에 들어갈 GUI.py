from tkinter import *

def click(key):
    if key == '지우기':
        entry.delete(0,END)
    elif key =='확인':
        get_cost=entry.get()
        print(get_cost)
    else:
        entry.insert(END,key)


window = Tk()
window.title("가계용 단말")
buttons = [
    '확인','1','2','3','4','5','6','7','8'
    ,'9','지우기','0','00'
    ]

#canvas_1 = Canvas(window, bg = 'grey', width = 700, height = 250) 기본크기.
canvas_2 = Canvas(window, bg = 'white', width = 200, height = 60)
canvas_3 = Canvas(window, bg = 'white', width = 200, height = 60)
canvas_4 = Canvas(window, bg = 'white', width = 200, height = 180)
entry = Entry(window, bg = 'white', width = 20)
canvas_6 = Canvas(window, bg = 'white', width = 200, height = 300)

canvas_2.grid(column=1, row=1)
canvas_3.grid(column=1, row=2)
canvas_4.grid(column=1, row=3, rowspan = 3)
canvas_6.grid(column=5, row=1, rowspan = 6)
entry.grid(column=2, row=1, columnspan = 2)
i = 0
a = 0
for b in buttons:
    cmd = lambda x=b: click(x)
    b = Button(window,text=b,width = 10,relief='ridge',command = cmd)
    if a == 0:
        b.grid(column=4,row=1)
        a+=1
    else:
        b.grid(row=i//3+2,column = i%3+2)
        i+=1

window.mainloop()
