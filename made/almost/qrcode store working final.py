from Tkinter import *
import qrcode
global img
storen=''

def click(key):
    if key == 'del':
        entry.delete(0,END)
    elif key =='check':
        global storen
        get_cost=entry.get()+'##'+storen
        print(get_cost)
        img = qrcode.make(get_cost)
        img.save("test.png")
    else:
        entry.insert(END,key)


def create(key):
    if key == 'create qrcode':
        photo = PhotoImage(file = "test.png")
        w = Label(window, image = photo)
        w.photo = photo
        w.grid(column = 5,row =2,rowspan=4)

def re_franchisee_code(key):
    if key == 'override':
        global storen
        fcode=entry.get()
        storen=fcode
        w = Label(window, text=fcode, font="times 20 italic")
        w.grid(column = 1,row =1,rowspan=1)
        
window = Tk()
window.title("store match")
buttons = [
    'check','1','2','3','4','5','6','7','8'
    ,'9','del','0','00'
    ]

#canvas_1 = Canvas(window, bg = 'grey', width = 700, height = 250) 기본크기.
canvas_3 = Button(window, text='override franchisee code', command = lambda y='override': re_franchisee_code(y))
canvas_2 = Canvas(window, bg = 'white', width = 200, height = 60)
canvas_4 = Canvas(window, bg = 'white', width = 200, height = 180)
entry = Entry(window, bg = 'white', width = 20)
canvas_6 = Canvas(window, bg = 'white', width = 200, height = 240)
check = Button(window, text = 'create qrcode',width = 20, command = lambda y='create qrcode': create(y))

canvas_2.grid(column=1, row=1)
canvas_3.grid(column=1, row=2)
canvas_4.grid(column=1, row=3, rowspan = 3)
canvas_6.grid(column=5, row=2, rowspan = 4)
entry.grid(column=2, row=1, columnspan = 2)
check.grid(column=5, row = 1)

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
