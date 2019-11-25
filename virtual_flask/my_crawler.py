from urllib.request import urlopen
from bs4 import BeautifulSoup



#<<<<<<< HEAD
html = urlopen('https://gs25.gsretail.com/gscvs/ko/membership-services/gift-certificate')
# gs 25 제휴카드 홈페이지
bsObject = BeautifulSoup(html, "html.parser")



# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
book_page_urls = []
for cover in bsObject.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page_urls.append(link)


# 메타 정보로부터 필요한 정보를 추출합니다.메타 정보에 없는 저자 정보만 따로 가져왔습니다.   
for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html, "html.parser")
    title = bsObject.find('meta', {'property':'rb:itemName'}).get('content')
    author = bsObject.select('span.name a')[0].text
    image = bsObject.find('meta', {'property':'rb:itemImage'}).get('content')
    url = bsObject.find('meta', {'property':'rb:itemUrl'}).get('content')
    originalPrice = bsObject.find('meta', {'property': 'rb:originalPrice'}).get('content')
    salePrice = bsObject.find('meta', {'property':'rb:salePrice'}).get('content')

    print(index+1, title, author, image, url, originalPrice, salePrice)



   # https://webnautes.tistory.com/691 코드의 원본 링크
   # https://bigfood.tistory.com/161 코드 참고 할 위치 해설 포함된 곳
   # https://docs.python.org/3.4/library/urllib.html 관련 문법 설치된 곳
#=======
html = urlopen('https://www.ivips.co.kr:7002/benefit/beCard.asp')
# 빕스 제휴 카드 홈페이지
bsobj = BeautifulSoup(html, "html.parser")


name=bsobj.findAll('th',{'scope':"row"})
get=bsobj.findAll('td',{'class':'ac-txt rline'})
detail=bsobj.findAll('ul',{'class':"list01"})
빕스=[]
for i in range(len(name)):
    빕스.append([0,0,0,0,0])
for x in range(len(name)):
    #print('==============================================================')
    #print(name[x].text,'\n' )
    빕스[x][0]=name[x].text.strip('\n \t \r')
    #print(get[x].text,'\n')
    빕스[x][4]=get[x].text+detail[x].text
    for i in range(5,100,5):
        if str(i)+'%할인' in get[x].text:
            빕스[x][2]='x*'+str((100-i)/100)
        if str(i)+'% 할인' in get[x].text:
            빕스[x][2]='x*'+str((100-i)/100)
    #print('==============================================================')
    #print('\n \n \n')
#print(빕스)
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
'''
for i in range(len(ls)):
    print(ls[i][0],'\t',ls[i][3])
print(ls[0][4])
'''
#>>>>>>> 5260af700a082e7bf629b88f0f4ac6cdbf339c4f
print("my_crawler.py complete")
