from urllib.request import urlopen
from bs4 import BeautifulSoup
import mongo_connection

html = urlopen('https://www.ivips.co.kr:7002/benefit/beCard.asp')
# 빕스 제휴 카드 홈페이지
'''
bsobj = BeautifulSoup(html, "html.parser")
body = bs.body

target = body.find(class_="lst_detaio_t1")

# ...
'''
name=bsobj.findAll('th',{'scope':"row"})
get=bsobj.findAll('td',{'class':'ac-txt rline'})
detail=bsobj.findAll('ul',{'class':"list01"})
빕스=[]
for i in range(len(name)):
    빕스.append([0,0,0,0,0])
for x in range(len(name)):
    빕스[x][0]=name[x].text.strip('\n \t \r')
    #print(get[x].text,'\n')
    빕스[x][4]=get[x].text+detail[x].text
    for i in range(5,100,5):
        if str(i) in get[x].text:
            빕스[x][2]='x*'+str((100-i)/100)

# 홈페이지에서 각각의 할인 정보를 추출하여 추출합니다.
#%% 데이터 저장 양식
'''
빕스[0][2]='x*1'
빕스[1][2]='x*1'
'''
a=['우리체크', 0 ,'x*0.8',0,'20프로 할인']
b=['우리신용', 10000 ,'x-3000.0',0,'결제 건당 3000원 할인']
c=['CU·배달의민족 삼성카드 taptap', 1500, 'x-(x//1500)*200',0,'1500원 당 200원 할인']
소지카드=['우리체크','CU·배달의민족 삼성카드 taptap']
편의점=[a,b,c]
스팅=[a,b,c]
주유소=[a,b,c]
가맹점명=["편의점", "주유소", "스팅", "빕스"]
가맹점=[편의점, 주유소, 스팅, 빕스]
#print(가맹점)

from def_cardlist_with_sort import *
imin="빕스"
ls=card_sort(where(imin, 가맹점명, 가맹점),  800000)
for i in range(len(ls)):
    print(ls[i][0],'\t',ls[i][3])
print(ls[0][4])
