# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:55:48 2019

@author: woneu
"""

import copy

personal_card=[['이마트 KB카드','<결제코드1>'],['삼성 S클래스 카드', '<켤제코드2>']]
def sending_data(personal_card):
    list=[]
    for i in len(personal_card):
        list.append(personal_card[i][1])
    return list

#get_from_personal= price, place, card data(edited by sending_data)
#from this line for server
빕스=[['CJ ONE 삼성카드', 0, 'x*0.7', 0, '최대30%할인+1%적립(적립은 CJ ONE포인트)\nCJ ONE 삼성카드 결제 시, 결제 금액에 대해 현장할인\n전월(1일~말일)실적 50만원 이상 결제회원 : 30%할인+1%적립\n전월(1일~말일)실적 20만원 이상 결제회원 : 20%할인+1%적립\n1일 1회(연12회) / 할인 전 식사금액 20만원 한도 내 \n할인 횟수 초과 시, 기본 적립률의 2배 적립\n'], ['CJ ONE 신한카드', 0, 'x*0.7', 0, '최대30%할인+1%적립(적립은 CJ ONE포인트)\nCJ ONE 신한카드 결제 시, 결제 금액에 대해 현장할인\n전월(1일~말일)실적 50만원 이상 결제회원 : 30%할인+1%적립\n전월(1일~말일)실적 20만원 이상 결제회원 : 20%할인+1%적립\n1일 1회(연12회) / 할인 전 식사금액 20만원 한도 내 \n할인 횟수 초과 시, 기본 적립률의 2배 적립\n'], ['The CJ카드', 0, 'x*0.8', 0, '20%할인+2%적립\nThe CJ카드로 결제 시 20%할인 및 The CJ카드 적립금 2%적립(KB국민카드, 현대카드, 신한카드, 삼성카드, SC비씨카드, 씨티카드, 하나카드, 롯데카드)\n1일 1회 식사금액 20만원 한도\nThe CJ카드 적립금은 빕스에서 현금처럼 사용 가능(단, CJ오쇼핑 회원에 한함)\nThe CJ카드 할인서비스와 카드사 포인트 차감결제 서비스 동시 사용 불가\n사용문의 : 080-000-6006\n'], ['신한 Lady카드', 0, 'x*0.8', 0, '20%할인\n월 2회, 연 6회 통합한도. 할인 전 식사금액 10만원 한도 내 할인\n전월(1일~말일) 30만원 이상 결제회원 대상\n신규 2개월간은 이용실적과 관계없이 서비스 제공(신규발급월 포함 최대 3개월)\n체크카드는 할인 적용대상에서 제외됨\n사용문의 : 1544-7000\n'], ['삼성 SFC', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n직전 3개월간 월 평균 30만원 이상 결제회원 대상\n발급 및 사용 문의 : 1588-8700\n'], ['삼성 T-Class Oil', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상\n신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월)\n발급 및 사용 문의 : 1588-8700\n'], ['삼성 Oil&Save Plus', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상\n단, 일부 카드는 직전 3개월간(1일~말일기준) 월평균 10만원 이상 이용회원 대상(은혜나눔 Oil & Save Plus) \n신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월)\n발급 및 사용문의 : 1588-8700\n'], ['삼성 S클래스카드', 0, 'x*0.8', 0, '20%할인\n1일 1회, 할인 전 식사금액 20만원 한도 내\n최근 3개월 간 (1일~말일 기준) 월 평균 30만원 이상 결제회원 대상\n신규 2개월간은 이용실적과 관계없이 서비스 제공 (신규발급월 포함 최대 3개월)\n타 제휴 할인 서비스와 동시에 사용 불가\n문의 : 1588-8700\n'], ['하나 Yes OK Saver', 0, 'x*0.8', 0, '20%할인\n통합 월 1회, 연 6회, 할인 전 식사금액 20만원 한도(월중 가장 먼저 승인된 패밀리 레스토랑에 대해서만 할인)\n전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경)\n신규 2개월간은 이용실적과 관계없이 서비스 제공 \n'], ['홈플러스 하나줄리엣카드', 0, 'x*0.8', 0, '20%할인\n통합 월 1회, 할인 전 식사금액 20만원 한도\n전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경)\n신규 2개월간은 이용실적과 관계없이 서비스 제공 \n'], ['하나 줄리엣카드 & Yes 4u shopping', 0, 'x*0.8', 0, '20%할인\n통합 월 1회, 할인 전 식사금액 20만원 한도\n전월(1일~말일) 30만원 이상 결제회원 대상(2012년 9월 1일부터 전월 실적 기준 변경)\n신규 2개월간은 이용실적과 관계없이 서비스 제공\n\n발급 및 사용문의: 1800-1111\n'], ['KB Star', 0, 'x*0.8', 0, '20%할인\nKB 스타카드로 결제 시 20% 할인 제공(체크카드 10%할인, 청구차감)\n엔터테인먼트 맞춤 할인 서비스 선택 회원에 한함 \n1일 1회, 할인 전 식사금액 20만원 한도\n발급 및 사용문의 : 1588-1688\nKB plusstar카드는 本 카드와 동일카드가 아님 : 할인불가 \nKB STAR max카드는 실적 구간별 청구서 할인 (本 카드와 동일카드 아님, 카드사 홈페이지 참고) \n'], ['이마트 KB카드', 0, 'x*0.85', 0, '15% 할인\n1인 1회, 할인전 식사금액 20만원 한도 내\n발급 및 사용문의 : 1588-1688\n']]
가맹점=[빕스]
가맹점명=['빕스']
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2][3]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num[3] < pivot:
            lesser_arr.append(num)
        elif num[3] > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

def card_sort(store, cost):        
    x=cost
    for i in range(len(store)):
        if x>=store[i][1]:
            realcost=eval(store[i][2])
        else:
            realcost=x
        store[i][3]=realcost
    sortcard=copy.deepcopy(store)
    return quick_sort(sortcard)

def where(place, 가맹점명, 가맹점):
    for i in range(len(가맹점명)):
        if 가맹점명[i]==place:
            return 가맹점[i]
    return -1
def do_con_have(sortedcard,mycard):
    for i in range(len(sortedcard)):
        if sortedcard[i][0] in mycard:
            x = i
            break
    return sortedcard[i][0]

def allin(price,place,concard,가맹점명, 가맹점):
    if where(place, 가맹점명, 가맹점)==-1:
        return '가맹점이 아닙니다.'
    else:
        ls=card_sort(where(place, 가맹점명, 가맹점), price)
        #print(ls)
        list=[]
        for i in ls:
            if i[0] in concard:
                list.append(i)
        if len(list)!=0:
            return list
        else:
            return '할인 받을 수 있는 카드가 없습니다.'
# 예시
#main
price=12000
place='빕스'
concard=['CJ ONE 신한카드','하나 Yes OK Saver']

print(allin(price,place,concard,가맹점명,가맹점))
