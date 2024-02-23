# 자 이번엔 월요일 웹툰들을 사전으로 저장해볼게요
# 우선 사이트 탐색을 해야죠!!
# https://comic.naver.com/webtoon/weekdayList.nhn?week=mon
# 우선 접속하고 봅시다!!
# Ctrl + 사이트클릭 하고 봅시다.
# <a href="/webtoon/list.nhn?titleId=758037&weekday=mon" title="참교육">
# 이부분을 긁어오면 되겠네요
# 이 태그 안에 titleId , 웹툰 제목이 있네요
# <div class="thumb"> 이라는 태그가 바로 위에 있네요
import requests
from bs4 import BeautifulSoup

url  = "https://comic.naver.com/webtoon/weekdayList.nhn?week=mon"
res = requests.get(url)
# print(res.text)
soup = BeautifulSoup(res.text,"html.parser")
# print(soup.select('div.thumb > a'))

웹툰사전 = {}

for i in soup.select('div.thumb > a'):
    #print(i)
    웹툰제목 = i.get('title') 
    웹툰번호 = i.get('href').split("titleId=")[1].split('&')[0]
    #print(웹툰제목, 웹툰번호)
    웹툰사전[웹툰제목] = 웹툰번호
print(웹툰사전)