# 167 번 파일을 폴더관리와 병합하여 
# 가수별로 폴더로 분류하고,
# 해당 가수 밑에 앨범 디렉터리들이 존재하고,
# 하위파일로 가사들을 저장하는 프로그램을 작성해보겠습니다.

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import os

def 폴더로설정불가한문자처리(폴더이름):
    문자목록 = "\\/:*?\"<>|"
    for i in 문자목록:
        폴더이름 = 폴더이름.replace(i,'')
    return 폴더이름


if not os.path.isdir("가사프로젝트"):  # 가사프로젝트 폴더가 없다면!
    os.mkdir("가사프로젝트")

검색어 = input("가수를 검색하세요 : ")

if not os.path.isdir(f"가사프로젝트/{검색어}"):
    os.mkdir(f"가사프로젝트/{검색어}")

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

if not os.path.isdir(f"가사프로젝트/{검색어}"):
    os.mkdir(f"가사프로젝트/{검색어}")
for i in soup.select(".spi_sns_share"):
    앨범경로 = i.get("data-url")
    앨범제목 = i.get("data-title")
    앨범제목 = 폴더로설정불가한문자처리(앨범제목)
    if not os.path.isdir(f"가사프로젝트/{검색어}/{앨범제목}"):
        os.mkdir(f"가사프로젝트/{검색어}/{앨범제목}")
        앨범사전[앨범제목] = 앨범경로

수록곡사전 = {}   
for 앨범제목 in 앨범사전:
    driver.get(앨범사전[앨범제목])
    sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    for i in soup.select(".inner_cell > a"):
        수록곡제목 = i.get('title')
        수록곡제목 = 폴더로설정불가한문자처리(수록곡제목)
        수록곡경로 = i.get('href')
        url = f"https://apis.naver.com/vibeWeb/musicapiweb{수록곡경로}/info"
        res = requests.get(url)
        if "<![CDATA[N]]>" in res.text:
            continue
        f = open(f"가사프로젝트/{검색어}/{앨범제목}/{수록곡제목}.txt","w",encoding="utf-8")
        가사 = res.text.split("<lyric><![CDATA[")[1].split(']]>')[0]
        f.write(가사)
        f.close()