from urllib.request import urlopen
from bs4 import BeautifulSoup



html = urlopen('https://www.ivips.co.kr:7002/benefit/beCard.asp')
# 빕스 제휴 카드 홈페이지
bsobj = BeautifulSoup(html, "html.parser")


name=bsobj.findAll('th',{'scope':"row"})
get=bsobj.findAll('td',{'class':'ac-txt rline'})
for x in range(len(name)):
    print('==============================================================')
    print(name[x].text,'\n' )
    print(get[x].text,'\n')
    print('==============================================================')
    print('\n \n \n')
# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
'''book_page_urls = []
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
'''
