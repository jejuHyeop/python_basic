# 149 파일을 import 해서 해도되는데
# 저는 숫자로 파일을 시작해버려서
# 물론 바꿀순있지만, 기능화는 여러분의 몫이라서
# 우선은 그냥 이 파일내에서 다 처리할게요

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
# 여기까지는 뭐라고요? 검증되서 건들 부분이 없어요
# 사전을 for 문으로 돌리면 key 값만 나와요 115 번파일을 보시면 
# 상세히 설명되어있습니다!!!!!!!! 복습!!!!
# 앞으로 dictionary 형 많이 사용할거에요
# 웹툰사전에 key, value 에 뭐가있는지 정리해보자구요

# 웹툰제목 : 웹툰번호
# key           value
# ~~/detail.nhn?titleId={}&no={}&weekday=mon
# 여기에 각각, 웹툰 번호와 화가 들어갑니다.
# 웹툰하나를 대상으로 1~3 을 조사하는거죠?
# 뭐가 많이 바껴요??
# no 이죠!!!
# 웹툰별 titleId 설정부분을 외반복문에 설정!!!
for i in 웹툰사전:
    for j in range(1,4):
        url  = f"https://comic.naver.com/webtoon/detail.nhn?titleId={웹툰사전[i]}&no={j}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "lxml")
        if len(soup.select("span#topPointTotalNumber")) == 0:   # 147 번파일 참조!!!! 크롤러를 좀 더 안전하게 만들어주죠!!
            break
        if res.url != url: # 147 번파일 참조!!!! 크롤러를 좀 더 안전하게 만들어주죠!!
            break 
        star = soup.select("span#topPointTotalNumber > strong")[0].text  # 145 파일에서 그대로 가져옴
        print(f"{i} {j}화 평점 : {star}")
        # 출력형식을 이쁘게
        # 무슨만화 몇화 평점 : ? 라고 해줄거에요

# 자, 무야호!!! 외쳐야하지 않겠습니까?
# 여러분의 처음 큰 프로젝트 코딩이었습니다~~
# 예외처리도 엄청잘되는거 보이실거에요
# ex) 2화까지 있는 친구도 에러없이 스무쓰하게 넘어갑니다.
