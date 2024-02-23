# 크롤링의 필수 : 실제 페이지를 열어놓고 비교해보기!!
# 가져오고싶은 페이지에 들어가셔서 F12 를 눌러줍니다.
# 웹에 표시된 내용 ( 웹 브라우저가 html 문서를 해석한 것!! )
# 은 무조건 html 안에 존재하기 때문에 지정만 해주면 되요
from bs4 import BeautifulSoup
import requests

# 자 우선, 코드를 짜기전에
# https://comic.naver.com/webtoon/detail.nhn?titleId=747269&no=49
# 이거 페이지를 켜주세요
# Ctrl 누른상태에서 9번째줄을 눌러주면 해당 페이지로 이동합니다!!

# STEP 1. 페이지 소스코드 받아오기!!!!
# requests.get 으로 하면되잖아요!!!
url = f"https://comic.naver.com/webtoon/detail.nhn?titleId=747269&no=49"
res = requests.get(url)


# STEP 2. 수시로 잘들어왔는지 확인하기!!!!!!!!
# 확인하는 습관이 얼마나 중요하냐면요
# 막 생각대로 짜다가 그 전에 짰던 코드들 전체를 확인하실래요?
# 아니면, 여기까지는 확실하니까 새로짠 코드가 무조건 문제구나!!!
# 19 번째 줄과 20 번째 줄의 상황은 진짜 완전 레알 달라요
# 19 번째 처럼 코딩을 해서 바로 나오면 좋지만
# 결국 좋은 개발자가 되기에는 한계가 있어요......................
# 모두 20 번째 줄 처럼 코딩하는 습관을 가져봐요!!
# print(res.text) # 잘 받아오나 확인!!!!!!!!!!!!!!!!!!!!
# 잘받아지면 그 때서야 주석처리하면 되잖아요

# STEP 3. 웹의 언어를 이해할 수 있는 녀석으로 처리하기
# 뭐해야된다고요? "파싱"
# "파싱"*100000000000000000000000000000000000000000000000000000
# 해야된다고요!!!
soup = BeautifulSoup(res.text, "html.parser")

# STEP 4. 이제 뽑아올 데이터의 특징점을 찾습니다.
# 평점이니까 그 주변으로 긁어올 포인트를 찾습니다.
# <span id="topPointTotalNumber">
#      <strong>9.98</strong>
# </span>
# 자 여기서 id 값을 기준으로 뽑아오면되겠네요!!
# selector 표현 기억나시죠!!!
#            " span#topPointTotalNumber " 이렇게 하면 된다구요!!!
soup.select("span#topPointTotalNumber")
# 여기까지 하면 뭐하시라구요?
# 확인하시라구요!!!!!!! 잘긁어오는지!!!!!!!!

# print(soup.select("span#topPointTotalNumber")) # 잘 긁어왔다면 주석처리를 그때서야 해주세요
# [<span id="topPointTotalNumber"><strong>9.98</strong></span>]
# 이게 나왔죠!!! 하나만 잘 나왔네요
# 만약에 여러값이 나온다면 원하는 값만 가져오면되요
# 아니면 selector 를 좀더 구체적으로 짜면되요!!!!!!!!!!!
# 불필요한 자료가 많이 걸러질 수록 
# 안좋은 크롤러를 만드는 거라는 걸 유념하세요!!!
# 앞에서 selector 가 무엇을 반환한다고요????????????????????
# Tag Class 자료들을 가지는 리스트!!!!!!!! 를 반환한다구요!!

# Tag Class!!
# HTML Tag 는 이렇게 구성되어있어요
# <a href="www.naver.com">Naver로 가기</a>

# a : 태그
# href : 속성
# www.naver.com : 속성값
# Naver로 가기 : text

# Tag class 의 핵심 속성 및 함수
# Tag.text             >  text 를 반환해요
# Tag.get(속성)    >  특정 속성의 속성값을 반환해요 

# 만약  <a href="www.naver.com">Naver로 가기</a>  를 대상으로 생각해볼게요
# i.text 를 하게되면 "Naver로 가기" 라는 text 가 나와요
# i.get('href') 를 하게되면 "www.naver.com" 가 나옵니다.
# 이거 두 개만 아시면되요!

# 즉!! 평점을 구하려면 strong 태그 안에 있는 text 값을 가져오면되요
print(soup.select("span#topPointTotalNumber > strong")[0].text)
print(soup.select("span#topPointTotalNumber")[0].text)
# 둘 다 상관은 없어요
# 왜냐하면 text 요소가 같기 때문이에요
# 하지만 만약!!!
# <span id="topPointTotalNumber">
#      <div> 평점은말이죠 </div>
#      <strong>9.98</strong>
# </span>
# 와 같은 구조에서 75, 76 코드를 실행하면 그 결과는 달라져요
# 81, 82 번째 줄에 각각 text 가 있으니 둘다 출력이 될겁니다.
# 말했죠!! 세세하게 나누는게 좋다구요!!!