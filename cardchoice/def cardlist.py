


a=['우리체크', 0 ,'x*0.8']
b=['우리신용', 10000 ,'x-3000.0']
c=['CU·배달의민족 삼성카드 taptap', 1500, 'x-(x//1500)*200']

편의점=[a,b,c]
스팅=[a,b,c]
주유소=[a,b,c]
가맹점명=["편의점", "주유소", "스팅"]
가맹점=[편의점, 주유소, 스팅]
x=10000

def where(place):
    for i in range(len(가맹점명)):
        if 가맹점명[i]==place:
            return 가맹점[i]
    return "가맹점이 아닙니다."

def card_choice(store, cost):        
    x=cost
    for i in range(len(store)):
        if x>=store[i][1]:
            realcost=eval(store[i][2])
        else:
            realcost=x
        store[i].append(realcost)

    for i in range(len(store)):
        if i==0:
            best=i
        else:
            if store[best][3]>store[i][3]:
                best=i
    return store[best][3], store[best][0]


imin="편의점"
ar,dr=card_choice(where(imin),12000)
print(ar,dr)
print(a[3],b[3],c[3])
