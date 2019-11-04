from tkinter import *
import qrcode
global img
def click(key):
    if key == '지우기':
        entry.delete(0,END)
    elif key =='확인':
        get_cost=entry.get()
        print(get_cost)
        img = qrcode.make(get_cost)
        img.save("test.png") #큐알코드 만들어서 저장. 가게이름도 받아야하는데..
    else:
        entry.insert(END,key)


'''def create(key):
    if key == 'create qrcode':
        photo = PhotoImage(file = "test.png")
        w = Label(window, image = photo)
        w.photo = photo
        w.grid(column = 5,row =2,rowspan=4)'''


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
canvas_6 = Canvas(window, bg = 'white', width = 200, height = 240)
#check = Button(window, text = 'create qrcode',width = 20, command = lambda y='create qrcode': create(y))

canvas_2.grid(column=1, row=1)
canvas_3.grid(column=1, row=2)
canvas_4.grid(column=1, row=3, rowspan = 3)
canvas_6.grid(column=5, row=2, rowspan = 4)
entry.grid(column=2, row=1, columnspan = 2)
#check.grid(column=5, row = 1)

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
