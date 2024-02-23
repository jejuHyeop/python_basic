# 162 번파일은 사실 그냥 value 가 리스트인 값을 다뤄보려고 했구요
# 저희 프로젝트에서는 수록곡 넘버를 가져오는 것이 목표입니다.
# 이부분은 스스로 찾아서 해보세요


from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://vibe.naver.com/artist/2475444/albums")
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "lxml")

앨범사전 = {}
for i in soup.select(".spi_sns_share"):
    앨범경로 = i.get("data-url")
    앨범제목 = i.get("data-title")
    앨범사전[앨범제목] = 앨범경로

# 여기까지는 161 번파일과 동일

수록곡사전 = {}   # key : 수록곡제목     ,     value : 수록곡경로
for i in 앨범사전:
    driver.get(앨범사전[i])
    sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    for j in soup.select(".inner_cell > a"):
        수록곡제목 = j.get('title')
        수록곡경로 = j.get('href')
        수록곡사전[수록곡제목] = 수록곡경로
print(수록곡사전)

# 이 파일까지 동적크롤링과 Dictionary 형을 다루는 방법에 대해서 어느정도 감이 생겼을 거에요 ^^ ~ 