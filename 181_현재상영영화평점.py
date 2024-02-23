import requests
from bs4 import BeautifulSoup
from time import sleep
import os

url = "https://movie.naver.com/movie/running/current.nhn"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

영화사전 = {}

def 문자열필터(st):                   # 읽어왔더니 더러운 값들이 많더라구요
    제거할문자 = "\t\n\r|"     # 그거 그냥 제거해줬습니다
    for i in 제거할문자:               # st 라는 문자가 들어오면 불필요한 것들 걸러주는
        st = st.replace(i,"")          # 함수에요~
    return st

for i in soup.select('dl.lst_dsc')[:10]:  # 영화 하나하나의 구간!! 이 담깁니다.
    영화제목 = i.select('dt.tit > a')[0].text
    영화평점 = i.select('span.num')[0].text
    평점참여 = i.select('.num2 > em')[0].text
    개요 = i.select('dl.info_txt1 > dd ')[0].text.split('분')
    상영시간 = 문자열필터(개요[0][-4:])
    개봉날짜 = 개요[1].split("개봉")
    개봉날짜 = 문자열필터(개봉날짜[0])
    영화감독 = 문자열필터(i.select('.link_txt')[1].text)
    
    영화사전[영화제목] = [영화평점, 평점참여, 상영시간, 개봉날짜, 영화감독]

while True:
    while True:
        print("="*30)
        print("현재 상영중인 영화 TOP 10")
        print("="*30)
        for num, i in enumerate(영화사전,1):
            print(f"{num}. {i}")
        user = input("번호 입력(종료 q) :")
        if user == 'q':
            exit()
        elif user.isnumeric():
            user = int(user)
            if 1<=user<=10:
                선택영화 = list(영화사전.keys())[user-1]
                print(f"{선택영화} 선택!!")
                sleep(1)
                os.system("cls")
                break
        else:
            print("입력이 바르지 않습니다.")
    print("="*50)
    print(f"{선택영화} Information")
    print("="*50)
    print("영화 평점 :", 영화사전[선택영화][0])
    print("평점 참여 관객수 :", 영화사전[선택영화][1])
    print("상영 시간 :", 영화사전[선택영화][2])
    print("개봉 날짜 :", 영화사전[선택영화][3])
    print("영화 감독 :", 영화사전[선택영화][4])
    input("다른 영화 알아보기!! (Enter)")
    os.system("cls")



# 영화감독을 뽑아내는게 제일 난관이었을 거에요.
# 왜냐하면, link_txt 를 가지는 요소들이 꽤 많기 때문인데요.
# 예를들어 개요, 출연진 또한 link_txt 를 가지고 있어요.
# 출연진의 수는 정확히 정해져있지 않아요.
# 그래서 처음에 soup.select(".link_txt") 로 접근하는 경우
# 출연진을 봤을 때 어떤 영화는 하나이고,
# 어떤 영화는 두개이기 때문에 
# 규칙성을 찾기가 힘듭니다.
# 예를들어 짝수 번째 link_txt 가 감독이야! 

# 이건 직접 구현을 안해보면 못느끼는 어려움이라서요 !! ㅜㅜ

# 그럼 어떻게 뽑아야 안전할까?
# 영화하나의 구간을 지정을 해서 안에서 읽으면 어떻게 되죠?
# 예를들어 하나의 영화를 대상으로
# 두 번째 값은 무조건 감독입니다.
# 이것으로 접근하셔야해요!!!
# 20 번째 줄을 해준 이유입니다.



