from tkinter import *
window = Tk()
# w = 700 h = 300
'''c1 = Canvas(window,bg = 'white', width = 300, height = 60)
c2 = Canvas(window ,bg = 'white', width = 300, height = 60)
c3 = Canvas(window,bg = 'white', width = 300, height = 60)
c4 = Canvas(window,bg = 'white', width = 150, height = 60)
c5 = Canvas(window, bg = 'white' , width = 150, height = 60)
c6 = Canvas(window, bg = 'white' , width = 150, height = 60)
c7 = Canvas(window, bg = 'white' , width = 150, height = 60)
c8 = Canvas(window, bg = 'white' , width = 300, height = 240)'''

c1 = Label(window,text='추천카드',bg = 'white', width = 40, height = 5)
c2 = Label(window,text='<추천카드 명 출력>',bg = 'white', width = 40, height = 5)
c3 = Label(window,text='<카드 혜택 출력>',bg = 'white', width = 40, height = 5)
c4 = Label(window,text='원 결제 금액',bg = 'white', width = 20, height = 5)
c5 = Label(window,text='<금액츨력>', bg = 'white' , width = 20, height = 5)
c6 = Label(window,text='실 결제 금액', bg = 'white' , width = 20, height = 5)
c7 = Label(window,text='<금액츨력>', bg = 'white' , width = 20, height = 5)
c8 = Label(window,text='결제 진행', bg = 'white' , width = 40, height = 20)

'''c1.create_text(30,10,text='추천카드')
c2.create_text(57,10,text='<추천카드 명 출력>')
c3.create_text(50,10,text='<카드 혜택 출력>')
c4.create_text(20,10,text='원 결제 금액')
c5.create_text(35,10,text='<금액츨력>')
c6.create_text(37,10,text='실 결제 금액')
c7.create_text(35,10,text='<금액츨력>')
c8.create_text(30,10,text='결제 진행')'''

c1.grid(column = 1, row = 1,columnspan = 2)
c2.grid(column = 1, row = 2,columnspan = 2)
c3.grid(column = 1, row = 3,columnspan = 2)
c4.grid(column = 1, row = 4)
c5.grid(column = 2, row = 4)
c6.grid(column = 1, row = 5)
c7.grid(column = 2, row = 5)
c8.grid(column = 3, row = 2, rowspan = 4, columnspan = 2)

b1 = Button(window, text = 'left')
b2 = Button(window, text = 'right')

b1.grid(column = 3, row =1)
b2.grid(column = 4, row =1)

window.mainloop()

'''고객용 단말에 필요한 기능.!'''
