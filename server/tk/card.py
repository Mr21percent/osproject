# -*- coding: utf-8 -*-

from Tkinter import *
import menu

def mod_card(signal):
	def read_txt(fname):
		openfile = open(fname, 'r')

		rstr = openfile.readlines()
		for i in range(len(rstr)):
			rstr[i] = rstr[i].strip().split(',')
		return rstr

		openfile.close()

	def write_txt(fname, lst):
		outfile = open(fname, 'w')

		sep = ','
		for i in lst:
			outfile.writelines(i[0] + sep + i[1] + '\n')

		outfile.close()


	window_col = Tk()

	leftF = Frame()
	leftF.pack(side=LEFT)

	F1 = Frame(leftF)
	scrollbar = Scrollbar(F1)
	listbox = Listbox(F1)

	scrollbar.pack(side=RIGHT, fill=Y)
	listbox.pack(side=LEFT, fill=Y)

	scrollbar['command'] = listbox.yview
	listbox['yscrollcommand'] = scrollbar.set

	# read data.txt
	filename = 'data.txt'
	data = read_txt(filename)
	data_origin = read_txt('data_origin.txt')
	for i in data_origin:
		listbox.insert(END, str(i[0]))
		F1.pack(side=TOP)


	rightF = Frame()
	rightF.pack(side=RIGHT, ipadx="3m", ipady="1m", padx="3m", pady="2m")

	def b1Click():
		global signal
		index = listbox.curselection()[0]
		card_name = data_origin[index][0]
		card_in_data = False
		for c in range(len(data)):
			if data[c][0] == card_name:
				card_in_data = True
				print("이미 저장된 카드")
				print(data)
				break
		if card_in_data == False:
			text = signal
			data.append([card_name, text])
			write_txt(filename, data)
			print("삽입 완료")
			print(data)

	def b2Click():
		index = listbox.curselection()[0]
		card_name = data_origin[index][0]
		card_in_data = False
		for c in range(len(data)):
			if data[c][0] == card_name:
				card_in_data = True
				del data[c]
				write_txt(filename, data)
				print("삭제 완료")
				print(data)
				break
		if card_in_data == False:
			print("저장되지 않은 카드")
			print(data)

	def b3Click():
		window_col.destroy()
		menu.mod_menu()

	b1 = Button(rightF, command=b1Click)  #카드추가
	b1.bind("<Return>", b1Click)
	b1.configure(text="카드복제", background="gray",
			width=6, padx="2m", pady="1m")
	b1.pack(side=TOP)

	b2 = Button(rightF, command=b2Click)   #카드삭제
	b2.bind("<Return>", b2Click)
	b2.configure(text="카드삭제", background="gray",
			width=6, padx="2m", pady="1m")
	b2.pack(side=TOP)

	b3 = Button(rightF, command=b3Click)
	b3.bind("<Return>", b3Click)
	b3.configure(text="메뉴", background="gray",
			width=6, padx="2m", pady="1m")
	b3.pack(side=TOP)


	window_col.mainloop()

