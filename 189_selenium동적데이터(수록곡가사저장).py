# 자 이제는 수록곡 별로 가사를 가져와볼건데요!! 
# 물론 selenium 으로 못하는 건 없지만, selenium 을 
# 굳이 사용하지 않아도 가져올 수 있는 방법은
# 수업시간에 설명드렸던
# Network Tab 에서 어느정도 해결할 수 있습니다.
# https://apis.naver.com/vibeWeb/musicapiweb/track/40550291/info 여기서 말이죠
# 여기는 굳이 동적데이터를 가져오지 않아도 되요
# requests 복습 들어갑니다.


from selenium import webdriver
from time import sleep
import requests
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

수록곡사전 = {}   
for i in 앨범사전:
    driver.get(앨범사전[i])
    sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    for j in soup.select(".inner_cell > a"):
        수록곡제목 = j.get('title')
        수록곡경로 = j.get('href')
        수록곡사전[수록곡제목] = 수록곡경로

# 여기까지는 164 번파일과 동일

가사사전 = {}           # key : 수록곡제목     ,      value : 가사
for i in 수록곡사전:
    url = f"https://apis.naver.com/vibeWeb/musicapiweb{수록곡사전[i]}/info"
    res = requests.get(url)
    # 이부분을 한번에 이해하기 어려우신 분은 우선 하나의 곡을 대상으로 테스트를 하면 되겠죠?
    if "<![CDATA[N]]>" in res.text:
        continue
    가사사전[i] = res.text.split("<lyric><![CDATA[")[1].split(']]>')[0].strip()
print(가사사전)



