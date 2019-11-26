from bs4 import BeautifulSoup
from urllib.request import urlopen

import mongo_connection
url = urlopen("https://movie.naver.com/movie/running/current.nhn")
bs = BeautifulSoup(url, 'html.parser')
body = bs.body

target = body.find(class_="lst_detail_t1")
list = target.find_all('li')

no = 1
for n in range(0, len(list)):
#print("======================")
#print("No.", no)
	no += 1
	# 영화 제목
	title = list[n].find(class_="tit").find("a").text
#print("영화 제목 :\t", title)
print(list)

'''
	# 감독
	try:
		director = list[n].find(class_="info_txt1").find_all("dd")[1].find("span").find_all("a")
		directorList = [director.text.strip() for director in director]
		print("제작 감독 :\t", directorList)
	except IndexError:
		print("제작 감독 :\t 정보 없음")
		directorList = "정보 없음"
	
	# 출연 배우
	try:
		cast = list[n].find(class_="lst_dsc").find("dl", class_="info_txt1").find_all("dd")[2].find(class_="link_txt").find_all("a")
		castList = [cast.text.strip() for cast in cast]
		print("출연 배우 :\t", castList)
	except IndexError:
		print("출연 배우 :\t 정보 없음")
		castList = "정보 없음"
	mongo_connection.save(title, directorList, castList)
'''
