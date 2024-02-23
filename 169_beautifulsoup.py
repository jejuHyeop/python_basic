# 자!!
# 웹브라우저가 하는 역할을 해주는 즉, html 를 해석해주는 녀석을 배우는 거에요
# python 의 입장에서는 Response.text 는 아무의미없는 문자들의 나열이에요
# 즉, <html>, <img>, <a> 그리고, 여러 속성들을 해석할 수 없어요
# 그냥 문자일뿐입니다.
# 이것을 '파싱' 해주어야한다고요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
# 파싱이란 자료의 특성에 맞게 해석하는 것을 말합니다. 파서는 파싱을 해주는 녀석입니다. 일종의 통역사죠!
# 그걸 BeautifulSoup 가 해줄거에요.
# 다시!!!! 뭐라구요?
# 무의미한 문자들의 나열을!!! 웹을 이해할 수 있도록 만들어준다고요!!!
# 그래야 특정 태그, 속성을 가진 녀석들을 가져와서 정보를 읽죠!!!!

from bs4 import BeautifulSoup         # 아 bs4 라는 파일에서 BeautifulSoup 라는 클래스를 가져오겠네?
                                                            # 어? 그럼 클래스의 인스턴스를 생성해서 뭘 하겠구나!!
import requests

naver = requests.get("https://www.naver.com")
soup = BeautifulSoup(naver.text, "html.parser")              # 여기서 naver.text 라구요!!!!!!!!!!!!!!!!!!!!!!!!!
                                                                                # 10번째줄을 다시 읽어보세요!!!!!
                                                                                # Response 객체를 넣는 실수!! 조심하세요
                                                                                # 오른쪽의 lxml 은 파서에요!!
                                                                                # html.parser 라는 녀석이 있지만
                                                                                # 최근 성능비교에서 lxml 이 뛰어나서 바꾼겁니다.
# 18 번째줄은 즉, naver.text 를 html.parser 형식으로 해석하는 녀석 soup 를 생성한거에요!!!
# soup 는 무의미한 문자들의 나열인 naver.text 를 웹의 언어대로 해석할 수 있습니다.
# 다음으로 이제 soup 에게 물어봐야겠죠?
# 내가 원하는 자료의 특징점을 찾아서 
# A 라는 자료 어딨어? B 라는 자료 어딨어?
# 이부분을 위해서는 ★★★★★★★★★★★★selector 표현을 알아야합니다!!!!
#★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★엄청중요합니다 여러분 셀렉터

# 자!!! 4가지만 알고갈게요. 원래 엄청 많아요..... 근데 대표적으로 4개만 쓰면 크롤링 가능합니다.
# [ rule1 ] 태그는 그냥 써주자
# [ rule2 ] id 속성은 # 를 사용하자
# [ rule3 ] class 속성은 . 를 사용하자
# [ rule4 ] 하위태그는 >(꺽새)를 사용하자

# rule1 의 다섯가지 예

# a 태그의 셀렉터표현 : a
# div 태그의 셀렉터표현 : div
# span 태그의 셀렉터표현 : span
# strong 태그의 셀렉터표현 : strong
# body 태그의 셀렉터표현 : body

# rule2 의 다섯가지 예

# hello1 이라는 id 셀렉터표현 : #hello1
# star 이라는 id 셀렉터표현 : #star
# python 이라는 id 셀렉터표현 : #python
# everyone 이라는 id 셀렉터표현 : #everyone
# fighting 이라는 id 셀렉터표현 : #fighting

# rule3 의 다섯가지 예

# hello1 이라는 class 셀렉터표현 : .hello1
# star 이라는 class 셀렉터표현 : .star
# python 이라는 class 셀렉터표현 : .python
# everyone 이라는 class 셀렉터표현 : .everyone
# fighting 이라는 class 셀렉터표현 : .fighting

# rule4 의 다섯가지 예

# div 태그 하위에 있는 span 태그 : div > span
# body 태그 하위에 있는 div 태그 : body > div
# div 태그 하위에 있는 a 태그 : div > a
# div 태그 하위에 있는 span 태그 하위에 있는 ul 태그 : div > span > ul
# body 하위에 table 하위에 div 하위에 span 하위에 ul 하위에 li : body > table > div > span > ul > li

# 여기서 주의!!
# <body>
#     <table>
#        <td>
#            <div>
#                <span>
#                        <ul>
#                             <li>
# 68 번째 줄 표현으로 다음의 코드의 li 태그를 읽어올 수 있을 까요?
# 안됩니다. 중간에 td 가 끼어있기 때문인데요.
# 중간에 생략 되는 태그가 없어야합니다.

# 추가!!
# 특정 태그 중 A 라는 id 를 가지는 태그 혹은
# 특정 태그 중 B 라는 class 를 가지는 태그를 지정해줄 수 있어요
# 예시를 보겠습니다.
# hello1 이라는 id를 가지는 div 태그 셀렉터표현 : div#hello1
# star 이라는 class를 가지는 span 태그 셀렉터표현 : span.star
# python 이라는 class를 가지는 a 태그 셀렉터표현 : a.python
# star 이라는 id를 가지는 strong 태그 셀렉터표현 : strong#star

# 이해하셨죠!!!
# 자 그럼 이걸 어디다 쓰냐
# soup 에는 select 라는 함수가 있는데요
# select 함수안에다 selector 표현을 써주시면되요

# soup.select([ selector 표현 ])
# ☆☆☆☆☆☆☆☆☆☆ 여기서 중요한건 select 의 반환형은
# 리스트라는 점이에요!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 나중에 코딩하다가 분명 실수할 부분이니 주의하세요.
# 각각의 자료들은 Tag 라는 클래스의 인스턴스들입니다!!!
# 100번째 줄은 좀 더 깊이 들어갈때 다룰게요