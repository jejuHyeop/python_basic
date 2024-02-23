# 일부러 이제야 나온만화를 가져왔어요
# https://comic.naver.com/webtoon/detail.nhn?titleId=769193&no=5
# 04-26 일 기준으로 4화까지밖에 안나왔네요
# 두 가지 상황에 대해서 제한이 있습니다. (더 많을 수도 있어요.. 그만큼 크롤링에는 예외가 생겨요)

# 상황1 ) 요소가 없어...
# 그럼 우선 이동을 해서 no 에 6,7,8 과 같은값을 줘보세요.
# 어떻게 되나요
# topPointTotalNumber 요소가 아예없어요
# 요소가 없는데 [0] 을 지정한다??


# 의미없는 크롤링...
# https://comic.naver.com/webtoon/detail.nhn?titleId=21815&no=768
# 상황2 ) 의미없는 크롤링...
# 다음으로 no 에 10000, 20000, 30000 과 같은값을 줘보세요.
# 어떻게 되나요
# 최신화가 나오죠?
# 즉, 1000000도 최신화로 이동하고 30000000도 최신화를 이동하기 때문에 같은화의 평점만 계속나와요
# 이건 간단하게 response 의 url 과 요청보낸 url 을 비교하면되겠죠?


# 상황1 이해더잘해보기!
# 다들 idle 창에서
# a = []
# a[0] 을 입력해보세요. 에러가나죠
# 즉, 요소가 없으면 그냥 끝내버리면되요


from bs4 import BeautifulSoup
import requests

N = int(input("화를 입력하세요 : "))

#상황1
for i in range(1, N+1):
    url = f"https://comic.naver.com/webtoon/detail.nhn?titleId=769193&no={i}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    if len(soup.select("span#topPointTotalNumber")) == 0:  # 상황1을 벗어나려면 이 코드를 넣어주면되죠!
        break 
    star = soup.select("span#topPointTotalNumber > strong")[0].text  # 145 파일에서 그대로 가져옴
    print(f"{i}화 평점 : {star}")

# 상황2
for i in range(768, N+768):
    url = f"https://comic.naver.com/webtoon/detail.nhn?titleId=21815&no={i}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")
    if res.url != url: # response 온 url 과 요청한 url 비교!!
        break 
    star = soup.select("span#topPointTotalNumber > strong")[0].text  # 145 파일에서 그대로 가져옴
    print(f"{i}화 평점 : {star}")

# 그럼 두 상황을 한 코드에 놔두면 비교적 안전한 크롤러가 되요