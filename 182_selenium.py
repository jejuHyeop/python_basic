# selenium 을 사용하는 경우 세가지를 볼게요
# 우선 selenium 은 브라우저를 동반한 Crawling 에서 사용하는 라이브러리입니다.
# 1. 로그인이 필요한 페이지에 접근하는 경우
# 2. 동적으로 정보를 받아오는 경우
# 3. 메뉴, 버튼등을 클릭하면서 정보를 끌어올때

# 브라우저를 동반하기때문에
# 기본적으로 웹 드라이버를 다운받아와야합니다.
# chromedriver.exe 를 기준으로 수업하겠습니다.
# 우선은 현재 Chrome 의 버전을 알아옵시다~
# Chrome 열어주시고, 도움말에 Chrome 정보를 클릭해보시면 현재 Chrome 의 버전이 나옵니다.
# 대부분 89.x.x.   90.x.x.  일겁니다~
# 구글에서 크롬 드라이버 다운로드를 검색해서
# https://chromedriver.chromium.org/downloads 이사이트에 접속해주세요
# 버전에 맞는 드라이버를 다운해주세요.
# 운영체제에 맞게 설치해주세요
# 그 뒤, 해당 폴더 안으로 넣어주세요.

from selenium import webdriver
from time import sleep                        # selenium 에서는 필수요소 입니다.

driver = webdriver.Chrome("chromedriver.exe")
url = "https://www.google.com"
driver.get(url)
driver.close()






