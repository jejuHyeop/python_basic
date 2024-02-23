# 153 파일에서 한단계 더 들어가서, 사용자가 q 를 입력할 때까지
# 웹툰을 다운받는 프로그램을 작성해봅시다.

import requests
from bs4 import BeautifulSoup
import os
from time import sleep

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
        for num,i in enumerate(웹툰사전,1):
            print(f"{num}. {i}")
        user = input("웹툰을 입력하세요(종료q) : ")
        if user == 'q':
            exit()
        if user.isnumeric():
            user = int(user)
            if 1 <= user <= num:
                선택한웹툰제목 = list(웹툰사전.keys())[int(user)-1]
                print(f"{선택한웹툰제목}을 다운로드 하겠습니다!!")
                break
        print("다시 입력해주세요.")

    N = int(input("다운받을 화를 입력하세요 : "))
    f = open(f"{선택한웹툰제목}_1to{N}.html","w",encoding="utf-8")

    for i in range(1,N+1):
        url = f"https://comic.naver.com/webtoon/detail.nhn?titleId={웹툰사전[선택한웹툰제목]}&no={i}"
        res = requests.get(url)
        if res.url != url:
            break
        f.write(res.text)
        print(f"{선택한웹툰제목} {i}화 Download 완료!")
    f.close()
    print("Download 완료 !!!")
    sleep(2)
    os.system("cls")