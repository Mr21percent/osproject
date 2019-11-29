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
vips=[]
for i in range(len(name)):
    vips.append([0,0,0,0,0])
for x in range(len(name)):
    vips[x][0]=name[x].text.strip('\n \t \r')
    vips[x][4]=get[x].text.strip('\n \t \r')+detail[x].text.strip('\n \t \r')
    for i in range(5,100,5):
        if str(i)+'%할인' in get[x].text:
            vips[x][2]='x*'+str((100-i)/100)
        if str(i)+'% 할인' in get[x].text:
            vips[x][2]='x*'+str((100-i)/100)
# 홈페이지에서 각각의 할인 정보를 추출하여 추출합니다.

'''
# vips.txt에 크롤링한 데이터 작성
fname = 'vips.txt'
outfile = open(fname, 'w')

sep = ','
for i in vips:
    res = i[4].split("\n")
    res2 = ' '.join(res)
    print(res2)
    outfile.writelines(i[0] + sep + str(i[1]) + sep + i[2] + sep + str(i[3]) + sep + res2 + '\n')

outfile.close()
'''


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

for i in vips:
    res = i[4].split("\n")
    i[4] = ' '.join(res)

print(vips)

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://fbtest-a36f5.firebaseio.com'
})

ref = db.reference() #db 위치 지정
ref.update({'빕스' : vips}) #해당 변수가 없으면 생성한다.

