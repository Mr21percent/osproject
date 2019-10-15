# 리스트 ['카드 이름', 금액 하안선, 실 거래가 계산식,(후에 실 거래가 계산)]
a=['우리체크', 0 ,'x*0.8']
b=['우리신용', 10000 ,'x-3000.0']
c=['CU·배달의민족 삼성카드 taptap', 1500, 'x-(x//1500)*200']
card_list=[a,b,c]
x=10000
for i in range(len(card_list)):
    if x>=card_list[i][1]:
        realcost=eval(card_list[i][2])
    else:
        realcost=x
    card_list[i].append(realcost)

for i in range(len(card_list)):
    if i==0:
        best=i
    else:
        if card_list[best][3]>card_list[i][3]:
            best=i

print(card_list[best][0],card_list[best][3])
            
print(a[3],b[3],c[3])
