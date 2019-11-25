from tkinter import *

window = Tk()

leftF = Frame()
leftF.pack(side=LEFT)

F1 = Frame(leftF)
scrollbar = Scrollbar(F1)
listbox = Listbox(F1)

scrollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=Y)

scrollbar['command'] = listbox.yview
listbox['yscrollcommand'] = scrollbar.set

for i in range(30):
	listbox.insert(END, str(i))

F1.pack(side=TOP)

F2 = Frame(leftF)
lab = Label(F2)

def poll():
	lab.after(200, poll)
	sel = listbox.curselection()
	lab.config(text = str(sel))

lab.pack()
F2.pack(side=TOP)

poll()

# ...

rightF = Frame()
rightF.pack(side=RIGHT, ipadx="3m", ipady="1m", padx="3m", pady="2m")

def b1Click():
	b1.configure(background="yellow")

def b2Click():
	b2.configure(background="blue")

b1 = Button(rightF, command=b1Click)
b1.bind("<Return>", b1Click)
b1.configure(text="카드복제", background="gray",
		width=6, padx="2m", pady="1m")
b1.pack(side=TOP)

b2 = Button(rightF, command=b2Click)
b2.bind("<Return>", b2Click)
b2.configure(text="취소", background="gray",
		width=6, padx="2m", pady="1m")
b2.pack(side=BOTTOM)



window.mainloop()
