# https://movie.naver.com/movie/running/current.nhn 
# 이 사이트 "현재상영영화" 들의 줄거리를 가져올겁니다.

import requests
from bs4 import BeautifulSoup

res = requests.get("https://movie.naver.com/movie/running/current.nhn")
soup = BeautifulSoup(res.text, "lxml")
영화사전 = {}
for i in soup.select("dt.tit > a"):
    영화제목 = i.text
    영화주소 = "https://movie.naver.com" + i.get("href")
    영화사전[영화제목] = 영화주소
print(영화사전)
# 여기서 11 번째 줄에서 code 를 분리해도 되지만, 
# 그냥 requests.get ( path ) 여기에 path 에 넣어줄 값을 완성해버리자구요!!

# 영화사전의 구성 key : 영화제목    value : 영화주소

영화내용 = {}
for i in 영화사전:
    res = requests.get(영화사전[i])          # url 이 value 잖아요!!
    soup = BeautifulSoup(res.text, "lxml")
    if len(soup.select("p.con_tx")) == 0:       # 만약 이 요소가 없다면
        continue
    줄거리 = soup.select('p.con_tx')[0].text
    영화내용[i] = 줄거리 #여기서 i 값에는 영화사전의 key 값인 영화제목이 들어가있어요
    print(f"{i} 줄거리 Crawling 완료!! ") # 확인하기 위해서!

while True:
    user = input("영화제목 입력 : ")
    if user in 영화내용:
        break
    print("해당하는 영화가 없습니다.")
print(f"줄거리 : {영화내용[user]}")

# 이것도 무한 루프로 사용자가 q 를 입력할 때까지 출력되게 해보세요!
