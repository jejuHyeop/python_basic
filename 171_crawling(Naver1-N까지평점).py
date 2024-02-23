# 그냥 no 인자를 반복만 해주면되요!!
from bs4 import BeautifulSoup
import requests

N = int(input("화를 입력하세요 : "))

for i in range(1, N+1):
    url = f"https://comic.naver.com/webtoon/detail.nhn?titleId=21815&no={i}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    star = soup.select("span#topPointTotalNumber > strong")[0].text  # 145 파일에서 그대로 가져옴
    print(f"{i}화 평점 : {star}")

# 자, 근데 예외가 있어요 만약, 이 웹툰이 10 화까지 나왔는데 20 을 입력하면 어떻게되요?
# 다음파일에서 다뤄볼게요