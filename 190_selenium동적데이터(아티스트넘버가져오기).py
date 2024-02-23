# 자 여기서 가수를 사용자에게 검색받고, 
# 해당 아티스트의 넘버를 알 수 있다면 무엇을 할 수 있을까요?

# 161 번 파일의 시작으로 165 번 까지 과정이 이어졌었죠??
# https://vibe.naver.com/artist/2475444/albums 
# 여기서 artist 뒤에 숫자만 바꾸면
# 가수의 모든 앨범을 가져올 수 있고, 수록곡도 가져올 수 있고, 가사도 가져올 수 있어요!!!!!!!!!!!!!!!!!!!!!1
# 자 여기서 소리한번 지르고 코딩합시다~~ 

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

검색어 = input("가수를 검색하세요 : ")

driver = webdriver.Chrome("chromedriver.exe")
driver.get(f"https://vibe.naver.com/search?query={검색어}")
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "lxml")
print(soup.select(".track_row")[0].get('href'))
# /artist/117564 이런 형태의 값이 나올 겁니다.
# https://vibe.naver.com/artist/2475444/albums 
# 여기서                           --------------------  여기만 바꿔주면 끝!