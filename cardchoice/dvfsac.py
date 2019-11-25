# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:08:20 2019

@author: woneu
"""
#%% 저장되어야 하는 데이터
빕스=[]
편의점=[]
가맹점=[빕스, 편의점]
가맹점명=['빕스', '편의점']
#%% 뭐냐 그 서버에서 데이터 관리 위한 코드
# for server i think 웹 크롤링
from urllib.request import urlopen
from bs4 import BeautifulSoup
import copy
def vips_card_crawl():
    html = urlopen('https://www.ivips.co.kr:7002/benefit/beCard.asp')
    bsobj = BeautifulSoup(html, "html.parser")
    name=bsobj.findAll('th',{'scope':"row"})
    get=bsobj.findAll('td',{'class':'ac-txt rline'})
    detail=bsobj.findAll('ul',{'class':"list01"})
    빕스=[]
    for i in range(len(name)):
        빕스.append([0,0,0,0,0])
    for x in range(len(name)):
        빕스[x][0]=name[x].text.strip('\n \t \r')
        빕스[x][4]=get[x].text+detail[x].text
        for i in range(5,100,5):
            if str(i) in get[x].text:
                빕스[x][2]='x*'+str((100-i)/100)
    return 빕스

빕스=vips_card_crawl()
#print(빕스)
#for i in
#%% 카드를 서버에서 정렬 해주는 코드
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
# 예시
con_have_card=['이마트 KB카드', '삼성 S클래스 카드']
con_pay_cost=80000
con_place='빕스'
if where(con_place, 가맹점명, 가맹점)==-1:
    print('가맹점이 아닙니다.')
else:
    ls=card_sort(where(con_place, 가맹점명, 가맹점), 12000)
    #ls=card_sort(where(con_place, 가맹점명, 가맹점),12000)
    print(ls)
'''
a=doihave(ls,소지카드)
print(a)
'''
#%% 개인 단말에서 구동시킬 코드
global i_have_card
i_have_card=[['이마트 KB카드', '<결제코드1>'],['삼성 S클래스 카드', '<켤제코드2>']]
def plus_card(name,signal):
    for i in range(len(i_have_card)):
        if name==i_have_card[i][0]:
            return print("it doesn't work")
    list=[]
    list.append(name)
    list.append(signal)
    i_have_card.append(list)
'''#위의 함수 검사
print(i_have_card)
plus_card('이마트 KB카드','<결제코드3>')
print(i_have_card)
'''
def rm_card(name):
    i = 0
    while i < len(i_have_card) :
        if(i_have_card[i][0] == name) :
            i_have_card.pop(i)
            i -= 1
        i += 1

'''# 위의 함수 검사
print(i_have_card)
rm_card('이마트 KB카드')
print(i_have_card)   
'''

#%% 개인 단말에서 구동시킬 코드