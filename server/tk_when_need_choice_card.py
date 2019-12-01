"""
Created on Wed Nov 20 16:29:02 2019

@author: woneu
"""
from tkinter import *
from mfrc522 import SimpleMFRC522
import threading
import RPi.GPIO as GPIO
from urllib.request import urlopen
from bs4 import BeautifulSoup

def read_txt(fname):
    openfile = open(fname, 'r')
    rstr = openfile.readlines()
    for i in range(len(rstr)):
        rstr[i] = rstr[i].strip().split(',')
    return rstr
    openfile.close()

def getting_card():
    filename = '/home/pi/gitproj/osproject/server/data.txt'
    data = read_txt(filename)
    data_origin = read_txt('data_origin.txt')
    for i in data_origin:
        listbox.insert(END, str(i[0]))
    F1.pack(side=TOP)
#print(ls)
GPIO.setwarnings(False)

def last_tk(oriprice, card_signal_data=getting_card()):

    html=urlopen('https://01031800998.localtunnel.me/readdb')
    bsobj=BeautifulSoup(html,"html.parser")
    #html="[['CJ ONE 삼성카드', 0, 'x*0.7', 105000.0, '최대30%할인+1%적립(적립은 CJ ONE포인트)CJ ONE 삼성카드 결제 시, 결제 금액에 대해 현장할인 전월(1일~말일)실적 50만원 이상 결제회원 : 30%할인+1%적립 전월(1일~말일)실적 20만원 이상 결제회원 : 20%할인+1%적립 1일 1회(연12회) / 할인 전 식사금액 20만원 한도 내 할인 횟수 초과 시, 기본 적립률의 2배 적립'], ['CJ ONE 신한카드', 0, 'x*0.7', 105000.0, '최대30%할인+1%적립(적립은 CJ ONE포인트)CJ ONE 신한카드 결제 시, 결제 금액에 대해 현장할인 전월(1일~말일)실적 50만원 이상 결제회원 : 30%할인+1%적립 전월(1일~말일)실적 20만원 이상 결제회원 : 20%할인+1%적립 1일 1회(연12회) / 할인 전 식사금액 20만원 한도 내 할인 횟수 초과 시, 기본 적립률의 2배 적립'], ['The CJ카드', 0, 'x*0.8', 120000.0, '20%할인+2%적립The CJ카드로 결제 시 20%할인 및 The CJ카드 적립금 2%적립(KB국민카드, 현대카드, 신한카드, 삼성카드, SC비씨카드, 씨티카드, 하나카드, 롯데카드) 1일 1회 식사금액 20만원 한도 The CJ카드 적립금은 빕스에서 현금처럼 사용 가능(단, CJ오쇼핑 회원에 한함) The CJ카드 할인서비스와 카드사 포인트 차감결제 서비스 동시 사용 불가 사용문의 : 080-000-6006'], ['신한 Lady카드', 0, 'x*0.8', 120000.0, '20%할인월 2회, 연 6회 통합한도. 할인 전 식사금액 10만원 한도 내 할인 전월(1일~말일) 30만원 이상 결제회원 대상 신규 2개월간은 이용실적과 관계없이 서비스 제공(신규발급월 포함 최대 3개월) 체크카드는 할인 적용대상에서 제외됨 사용문의 : 1544-7000'], ['삼성 SFC', 0, 'x*0.8', 120000.0, '20%할인1일 1회, 할인 전 식사금액 20만원 한도 내 직전 3개월간 월 평균 30만원 이상 결제회원 대상 발급 및 사용 문의 : 1588-8700'], ['삼성 T-Class Oil', 0, 'x*0.8', 120000.0, '20%할인1일 1회, 할인 전 식사금액 20만원 한도 내 최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상 신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월) 발급 및 사용 문의 : 1588-8700'], ['삼성 Oil&Save Plus', 0, 'x*0.8', 120000.0, '20%할인1일 1회, 할인 전 식사금액 20만원 한도 내 최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상 단, 일부 카드는 직전 3개월간(1일~말일기준) 월평균 10만원 이상 이용회원 대상(은혜나눔 Oil & Save Plus) 신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월) 발급 및 사용문의 : 1588-8700'], ['삼성 S클래스카드', 0, 'x*0.8', 120000.0, '20%할인1일 1회, 할인 전 식사금액 20만원 한도 내 최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상 신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월) 타 제휴 할인 서비스와 동시에 사용 불가 문의 : 1588-8700'], ['하나 Yes OK Saver', 0, 'x*0.8', 120000.0, '20%할인통합 월 1회, 연 6회, 할인 전 식사금액 20만원 한도(월중 가장 먼저 승인된 패밀리 레스토랑에 대해서만 할인) 전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경) 신규 2개월간은 이용실적과 관계없이 서비스 제공'], ['홈플러스 하나줄리엣카드', 0, 'x*0.8', 120000.0, '20%할인통합 월 1회, 할인 전 식사금액 20만원 한도 전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경) 신규 2개월간은 이용실적과 관계없이 서비스 제공'], ['하나 줄리엣카드 & Yes 4u shopping', 0, 'x*0.8', 120000.0, '20%할인통합 월 1회, 할인 전 식사금액 20만원 한도 전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경) 신규 2개월간은 이용실적과 관계없이 서비스 제공 발급 및 사용문의: 1800-1111'], ['KB Star', 0, 'x*0.8', 120000.0, '20%할인KB 스타카드로 결제 시 20% 할인 제공(체크카드 10%할인, 청구차감) 엔터테인먼트 맞춤 할인 서비스 선택 회원에 한함 1일 1회, 할인 전 식사금액 20만원 한도 발급 및 사용문의 : 1588-1688 KB plusstar카드는 本 카드와 동일카드가 아님 : 할인불가 KB STAR max카드는 실적 구간별 청구서 할인 (本 카드와 동일카드 아님, 카드사 홈페이지 참고)'], ['이마트 KB카드', 0, 'x*0.85', 127500.0, '15% 할인1인 1회, 할인전 식사금액 20만원 한도 내 발급 및 사용문의 : 1588-1688']]"
    #bsobj=BeautifulSoup(html,"html.parser")
    a=str(bsobj).replace("'","\n")
    a=a.replace(",","")
    a=a.replace("[","") 
    a=a.replace("]","")
    b=a.split("\n")
    k=[]
    for i in b:
        if i=="" or i==' ':
            b.remove(i)
    for i in range(len(b)//5):
        k.append([0,0,0,0,0])
    for i in range(len(b)):
        k[i//5][i%5]=b[i]
    concard=[]
    for i in card_signal_data:
        concard.append(i[0])
    mci=[]
    for i in k:
        if i[0] in concard:
            mci.append(i)
    if len(mci)==0:
        window2 = Tk()
        window2.title("none")
        window2.resizable(False,False)

        label=Label(window2, text="해당되는 카드가 존재하지 않습니다.", width=10, height=5)
        label.pack()
        window2.mainloop()
    else:
        window = Tk()
        # w = 700 h = 300
        nu=0
        def nextc():
            nonlocal nu
            nu-=1
            nonlocal mci
            nu=nu%len(mci)
            print(nu)
            c2["text"]=mci[nu][0]
            c3["text"]=mci[nu][4]
            c7["text"]=mci[nu][3]

        def backc():
            nonlocal nu
            nu+=1
            nonlocal mci
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
            nonlocal nu
            k = threading.Thread(target=RFID_WRITE,name = "RFID",args=(card_signal_data[nu][1],24,23,19,21,22))
            k.start()
	#write name of card on rfid card
	# need to get mci from another file and card_signal_data, oriprice

        c1 = Label(window,text='추천카드',bg = 'white', width = 40, height = 5)
        c2 = Label(window,text=mci[nu][0],bg = 'white', width = 40, height = 5)
        c3 = Label(window,text=mci[nu][4],bg = 'white', width = 40, height = 15, wraplength=200)
        c4 = Label(window,text='원 결제 금액',bg = 'white', width = 20, height = 5)
        c5 = Label(window,text=oriprice, bg = 'white' , width = 20, height = 5)
        c6 = Label(window,text='실 결제 금액', bg = 'white' , width = 20, height = 5)
        c7 = Label(window,text=mci[nu][3], bg = 'white' , width = 20, height = 5)
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
