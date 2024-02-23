# 아이즈원의 앨범목록 및 앨범경로를 가져와서 Dict 형으로 저장해볼까요
# vibe 를 통해서 가져올게요
# (더좋은 사이트가 있으면 다른걸 이용하세요)
# 사이트에 들어가서 우선은 해당 페이지에
# 앨범 넘버와 관련된 요소가 어디어디 있고,
# 어떤 태그를 가져와야 효율적일지를 판단해보세요!!

# 저는 .title 보단 .spi_sns_share 로 진행하겠습니다.
# 왜냐하면 앨범제목과 url 이 동시에 있기 때문이에요

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
#    print(앨범경로, 앨범제목) # 우선 확인!
    앨범사전[앨범제목] = 앨범경로
print(앨범사전)