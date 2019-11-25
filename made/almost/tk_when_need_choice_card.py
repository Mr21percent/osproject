# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 16:29:02 2019

@author: woneu
"""

from tkinter import *
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
    
def makesignal():
    print(card_signal_data[nu])
    #need to change to make sigal
    
mci=[
 ['CJ ONE 삼성카드', 0, 'x*0.7', 0, '최대30%할인+1%적립(적립은 CJ ONE포인트)\nCJ ONE 삼성카드 결제 시, 결제 금액에 대해 현장할인\n전월(1일~말일)실적 50만원 이상 결제회원 : 30%할인+1%적립\n전월(1일~말일)실적 20만원 이상 결제회원 : 20%할인+1%적립\n1일 1회(연12회) / 할인 전 식사금액 20만원 한도 내 \n할인 횟수 초과 시, 기본 적립률의 2배 적립\n'], 
 ['CJ ONE 신한카드', 0, 'x*0.7', 0, '최대30%할인+1%적립(적립은 CJ ONE포인트)\nCJ ONE 신한카드 결제 시, 결제 금액에 대해 현장할인\n전월(1일~말일)실적 50만원 이상 결제회원 : 30%할인+1%적립\n전월(1일~말일)실적 20만원 이상 결제회원 : 20%할인+1%적립\n1일 1회(연12회) / 할인 전 식사금액 20만원 한도 내 \n할인 횟수 초과 시, 기본 적립률의 2배 적립\n'], 
 ['The CJ카드', 0, 'x*0.8', 0, '20%할인+2%적립\nThe CJ카드로 결제 시 20%할인 및 The CJ카드 적립금 2%적립(KB국민카드, 현대카드, 신한카드, 삼성카드, SC비씨카드, 씨티카드, 하나카드, 롯데카드)\n1일 1회 식사금액 20만원 한도\nThe CJ카드 적립금은 빕스에서 현금처럼 사용 가능(단, CJ오쇼핑 회원에 한함)\nThe CJ카드 할인서비스와 카드사 포인트 차감결제 서비스 동시 사용 불가\n사용문의 : 080-000-6006\n'],
 ['신한 Lady카드', 0, 'x*0.8', 0, '20%할인\n월 2회, 연 6회 통합한도. 할인 전 식사금액 10만원 한도 내 할인\n전월(1일~말일) 30만원 이상 결제회원 대상\n신규 2개월간은 이용실적과 관계없이 서비스 제공(신규발급월 포함 최대 3개월)\n체크카드는 할인 적용대상에서 제외됨\n사용문의 : 1544-7000\n'],
 ['삼성 SFC', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n직전 3개월간 월 평균 30만원 이상 결제회원 대상\n발급 및 사용 문의 : 1588-8700\n'],
 ['삼성 T-Class Oil', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상\n신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월)\n발급 및 사용 문의 : 1588-8700\n'],
 ['삼성 Oil&Save Plus', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상\n단, 일부 카드는 직전 3개월간(1일~말일기준) 월평균 10만원 이상 이용회원 대상(은혜나눔 Oil & Save Plus) \n신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월)\n발급 및 사용문의 : 1588-8700\n'],
 ['삼성 S클래스카드', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상\n신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월)\n타 제휴 할인 서비스와 동시에 사용 불가\n문의 : 1588-8700\n'],
 ['하나 Yes OK Saver', 0, 'x*0.8', 0, '20%할인\n통합 월 1회, 연 6회, 할인 전 식사금액 20만원 한도(월중 가장 먼저 승인된 패밀리 레스토랑에 대해서만 할인)\n전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경)\n신규 2개월간은 이용실적과 관계없이 서비스 제공 \n'],
 ['홈플러스 하나줄리엣카드', 0, 'x*0.8', 0, '20%할인\n통합 월 1회, 할인 전 식사금액 20만원 한도\n전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경)\n신규 2개월간은 이용실적과 관계없이 서비스 제공 \n'],
 ['하나 줄리엣카드 & Yes 4u shopping', 0, 'x*0.8', 0, '20%할인\n통합 월 1회, 할인 전 식사금액 20만원 한도\n전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경)\n신규 2개월간은 이용실적과 관계없이 서비스 제공\n\n발급 및 사용문의: 1800-1111\n'],
 ['KB Star', 0, 'x*0.8', 0, '20%할인\nKB 스타카드로 결제 시 20% 할인 제공(체크카드 10%할인, 청구차감)\n엔터테인먼트 맞춤 할인 서비스 선택 회원에 한함 \n1일 1회, 할인 전 식사금액 20만원 한도\n발급 및 사용문의 : 1588-1688\nKB plusstar카드는 本 카드와 동일카드가 아님 : 할인불가 \nKB STAR max카드는 실적 구간별 청구서 할인 (本 카드와 동일카드 아님, 카드사 홈페이지 참고) \n'],
 ['이마트 KB카드', 0, 'x*0.85', 0, '15% 할인\n1인 1회, 할인전 식사금액 20만원 한도 내\n발급 및 사용문의 : 1588-1688\n']
]
card_signal_data=[
 ['CJ ONE 삼성카드', 'signal1'], 
 ['CJ ONE 신한카드', 'signal2'], 
 ['The CJ카드',' signal3'],
 ['신한 Lady카드','signal4'],
 ['삼성 SFC','signal5'],
 ['삼성 T-Class Oil','signal6'],
 ['삼성 Oil&Save Plus','signal7'],
 ['삼성 S클래스카드', 'signal8'],
 ['하나 Yes OK Saver','signal9'],
 ['홈플러스 하나줄리엣카드','signal10'],
 ['하나 줄리엣카드 & Yes 4u shopping','signal11'],
 ['KB Star','signal12'],
 ['이마트 KB카드', 'signal13']
]
oriprice=10000

# need to get mci from another file and card_signal_data, oriprice

c1 = Label(window,text='추천카드',bg = 'white', width = 40, height = 5)
c2 = Label(window,text=mci[nu][0],bg = 'white', width = 40, height = 5)
c3 = Label(window,text=mci[nu][4],bg = 'white', width = 40, height = 5)
c4 = Label(window,text='원 결제 금액',bg = 'white', width = 20, height = 5)
c5 = Label(window,text=oriprice, bg = 'white' , width = 20, height = 5)
c6 = Label(window,text='실 결제 금액', bg = 'white' , width = 20, height = 5)
c7 = Label(window,text=mci[nu][3], bg = 'white' , width = 20, height = 5)
c8 = Button(window,text='결제 진행', bg = 'white' , width = 40, height = 20, command = makesignal)


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

'''고객용 단말에 필요한 기능.!'''