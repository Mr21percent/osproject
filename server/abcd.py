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
#가맹점=[빕스]
#가맹점명=['vips']
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

def allin(price,place,가맹점명, 가맹점):
    if where(place, 가맹점명, 가맹점)==-1:
        return '가맹점이 아닙니다.'
    else:
        ls=card_sort(where(place, 가맹점명, 가맹점), price)
        return ls
		#print(ls)
        list=[]
        if len(list)!=0:
            return list
        else:
            return '할인 받을 수 있는 카드가 없습니다.'

# 예시
#main
#price=12000
#place='빕스'
#concard=['CJ ONE 신한카드','하나 Yes OK Saver']

#print(allin(price,place,concard,가맹점명,가맹점))
