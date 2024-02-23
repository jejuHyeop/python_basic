# 활용2. 웹툰과 화를 입력받고, 해당 웹툰의 특정화까지 한페이지에 다운로드
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
        print(웹툰번호)
        웹툰사전[웹툰제목] = 웹툰번호


while True:
    user = input("웹툰을 입력하세요 : ")
    if user in 웹툰사전:
        break
    print("해당 웹툰이 없습니다.")
N = int(input("화를 입력하세요 : "))

f = open(f"{user}_1to{N}.html","w",encoding="utf-8")

for i in range(1,N+1):
    url = f"https://comic.naver.com/webtoon/detail.nhn?titleId={웹툰사전[user]}&no={i}"
    res = requests.get(url)
    if res.url != url:
        break
    f.write(res.text)
    print(f"{user} {i}화 Download 완료!")

f.close()