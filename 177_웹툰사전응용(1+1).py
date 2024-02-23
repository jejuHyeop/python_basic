# 151 파일에서 한단계 더 들어가서, 사용자가 q 를 입력할 때까지
# 웹툰을 읽어오는 프로그램을 작성해봅시다. 

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

while True:
    while True:
        user = input("웹툰을 입력하세요(종료q) : ")
        if user in 웹툰사전:           # 웹툰이 있거나 q 를 누르면 나가게 해야함으로!! exit(0)
            break
        if user == 'q':
            exit()                          # 프로그램을 종료하는 명령어 입니다~ break 를 사용해도 되지만
                                               # 하나의 반복문만 break 되기 때문에 그냥 exit 해버리죠! 
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

