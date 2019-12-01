"""
Created on Wed Nov 20 16:29:02 2019
@author: woneu
"""
from tkinter import *
from mfrc522 import SimpleMFRC522
import threading
import RPi.GPIO as GPIO
from urllib.request import urlopen
#from bs4 import BeautifulSoup



#print(ls)
GPIO.setwarnings(False)
mci = [['sdfasfd',1231,'x-10',0,'dfaf']]
oriprice = 1230345
window = Tk()
# w = 700 h = 300
nu=0
def nextc():
    global nu
    nu-=1
    global mci
    nu=nu%len(mci)
    print(nu)
    c2["text"]=mci[nu][0]
    c3["text"]=mci[nu][4]
    c7["text"]=mci[nu][3]

def backc():
    global nu
    nu+=1
    global mci
    nu=nu%len(mci)
    print(nu)
    c2["text"]=mci[nu][0]
    c3["text"]=mci[nu][4]
    c7["text"]=mci[nu][3]

def RFID_WRITE(T,SDA,SCK,MOSI,MISO,RST):
    reader = SimpleMFRC522()
    text = T
    reader.write(text)
    print("Written")
#There is some warning points simpleMFRC522 can't read or write type: int

def RFID_READ(SDA,SCK,MOSI,MISO,RST):
    reader = SimpleMFRC522()
    id, text = reader.read()
    print(id)
    print(text)


        #Tell a text, and Count the text
                        
def makesignal():
    global nu
    k = threading.Thread(target=RFID_WRITE,name="RFID",args=(mci[nu][0],24,23,19,21,22))
    k.start()
    #write name of card on rfid card
	# need to get mci from another file and card_signal_data, oriprice

c1 = Label(window,text='추천카드',bg = 'white', width = 40, height = 5)
c2 = Label(window,text=mci[nu][0],bg = 'white', width = 40, height = 5)
c3 = Label(window,text=mci[nu][4],bg = 'white', width = 40, height = 15, wraplength=200)
c4 = Label(window,text='원 결제 금액',bg = 'white', width = 20, height = 5)
c5 = Label(window,text=oriprice, bg = 'white' , width = 20, height = 5)
c6 = Label(window,text='실 결제 금액', bg = 'white' , width = 20, height = 5)
c7 = Label(window,text=int(mci[nu][3]), bg = 'white' , width = 20, height = 5)
c8 = Button(window,text='결제 진행', bg = 'white' , width = 40, height = 30, command = makesignal)


c1.grid(column = 1, row = 1,columnspan = 2)
c2.grid(column = 1, row = 2,columnspan = 2)
c3.grid(column = 1, row = 3,columnspan = 2)
c4.grid(column = 1, row = 4)
c5.grid(column = 2, row = 4)
c6.grid(column = 1, row = 5)
c7.grid(column = 2, row = 5)
c8.grid(column = 3, row = 2, rowspan = 4, columnspan = 2)
b1 = Button(window, text = 'back', command = nextc)
b2 = Button(window, text = 'next', command = backc)

b1.grid(column = 3, row =1)
b2.grid(column = 4, row =1)

window.mainloop()

'''
고객용 단말에 필요한 기능.!
'''
