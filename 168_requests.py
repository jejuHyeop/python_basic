# Client 가 Server 에게 request 하는 것을 도와주는 라이브러리입니다
import requests

url = "https://www.naver.com"
res = requests.get(url) # 이런식으로 url 을 넣어주면, 반환값으로 Response 객체를 반환합니다.
                                    # response 객체를 !!!!!! 반환한다구요

print(type(res))      # Response 객체임을 확인
print(dir(res))          # response 객체면 가져야하는 속성과 함수들을 볼 수 있어요

# 그 중에 Response.text 를 보자구요!
# Web Page 에서 F12 를 누르면, 나오는 녀석들이 Response.text 입니다.
print(res.text)
# 바로이 html 을 웹 브라우저(Chrome, IE, FireFox, Safari) 들이 해석해서 이쁘게 출력해주는거에요