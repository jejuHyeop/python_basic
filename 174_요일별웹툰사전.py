# url 파악이 정말 재밌고 신기한게, 잘보시면 다 규칙이있어요
# 월 : https://comic.naver.com/webtoon/weekdayList.nhn?week=mon
# 화 : https://comic.naver.com/webtoon/weekdayList.nhn?week=tue
# 수 : https://comic.naver.com/webtoon/weekdayList.nhn?week=wed
# 목 : https://comic.naver.com/webtoon/weekdayList.nhn?week=thu
# 금 : https://comic.naver.com/webtoon/weekdayList.nhn?week=fri
# 토 : https://comic.naver.com/webtoon/weekdayList.nhn?week=sat
# 일 : https://comic.naver.com/webtoon/weekdayList.nhn?week=sun
# 마지막 week 인자만 바껴요!!!
# 저거 반복해주면되죠?
# 리스트로 구현해줄게요

# 자, 여러분 148 번째 코드에서
# 월요일 사전 만드는거 성공했죠?
# 그럼!! 확실히 돌아가는걸 확실하게 짜셨으니까
# 중간중간에 print 해주지 않아도되요
# 이게 제가 말했던 기능화이고요.
# 정확한 코드는 믿어도되요! 코드를 한줄한줄 이해한 자만이
# 흔들리지 않습니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1

# 다른점이 있다면 사전을 초기화하는위치!! 조심하세요
# 28 번째 줄 즉, 반복문에서 빼주셔야 쌓이겠죠?


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

print(웹툰사전) # 이건 확인 새로 해주셔야죠!