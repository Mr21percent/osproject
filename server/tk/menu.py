# -*- coding: utf-8 -*-

from Tkinter import *
import test, card, read_qr

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

class RFID:
	def Write(self,T):
		reader = SimpleMRFC522()
		text = T
		reader.write(text)
		print("written")

	def Read(self):
		reader = SimpleMFRC522()
		id, text = reader.read()
		return text

def mod_menu():
	window_menu = Tk()

	c1 = Canvas(window_menu, bg = 'white', width = 300, height = 60)
	c2 = Canvas(window_menu, bg = 'white', width = 300, height = 60)

	s = RFID()
	signal = s.Read()

	def b1Click():
		nonlocal signal
		window_menu.destroy()
		card.mod_card(signal)

	def b2Click():
		window_menu.destroy()
		p,s = read_qr.readQR()
		read_qr.uploadDB(p,s)
		read_qr.open_web()


	b1 = Button(window_menu, command = b1Click)
	b1.bind("<Return>", b1Click)
	b1.configure(text="카드입력", background="gray")
	b1.pack(side=LEFT)


	b2 = Button(window_menu, command = b2Click)
	b2.bind("<Return>", b2Click)
	b2.configure(text="결제", background="gray")
	b2.pack(side=RIGHT)


	window_menu.mainloop()

