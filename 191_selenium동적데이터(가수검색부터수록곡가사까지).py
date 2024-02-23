from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

검색어 = input("가수를 검색하세요 : ")

driver = webdriver.Chrome("chromedriver.exe")
driver.get(f"https://vibe.naver.com/search?query={검색어}")
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "lxml")
아티스트넘버 = soup.select(".track_row")[0].get('href')

driver.get(f"https://vibe.naver.com{아티스트넘버}/albums")
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

가사사전 = {}           
for i in 수록곡사전:
    url = f"https://apis.naver.com/vibeWeb/musicapiweb{수록곡사전[i]}/info"
    res = requests.get(url)
    if "<![CDATA[N]]>" in res.text:
        continue
    가사사전[i] = res.text.split("<lyric><![CDATA[")[1].split(']]>')[0].strip()
print(가사사전)

while True:
    while True:
        user = input("노래검색 : ")
        if user in 가사사전:
            break
        print("그런 노래 없습니다.")
    print(가사사전[user])
