# 웹툰 사전을 만들면 다음과 같이 활용할 수 있을 것입니다.
# 149 번파일 import 를 통해서 진행하셔도됩니다.

# 활용1. 웹툰과 화를 입력받고, 해당 웹툰의 특정화까지 평점을 구해주는 프로그램

import requests
from bs4 import BeautifulSoup

요일 = ["mon","tue","wed","thu","fri","sat","sun"]
웹툰사전 = {}

for i in 요일:
    url  = f"https://comic.naver.com/webtoon/weekdayList.nhn?week={i}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    for j in soup.select('div.thumb > a'):
        웹툰제목 = j.get('title') 
        웹툰번호 = j.get('href').split("titleId=")[1].split('&')[0]
        웹툰사전[웹툰제목] = 웹툰번호

# 여기까지 149 번 파일 

while True:
    user = input("웹툰을 입력하세요 : ")
    if user in 웹툰사전:
        break
    print("해당 웹툰이 없습니다.")
N = int(input("화를 입력하세요 : "))

for i in range(1,N+1):
    url = f"https://comic.naver.com/webtoon/detail.nhn?titleId={웹툰사전[user]}&no={i}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    if len(soup.select("#topPointTotalNumber > strong")) == 0:
        break
    if res.url != url:
        break
    star = soup.select("#topPointTotalNumber > strong")[0].text
    print(f"{user} {i}화 평점 {star}")

