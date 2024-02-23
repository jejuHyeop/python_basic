# 물론 한글에서 단어라함은 조사나 그런것들을 제거하는것 까지 생각하는데
# 그부분은 좀더 정교한 라이브러리들을 찾아보면 나올겁니다! 
# 기본적인 것만 없애볼게요
# 그냥 공백을 기준으로 해볼게요.

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import turtle as t
import random as r

def 거르자(가사):
    걸러야할단어목록 = "()_!?,"
    for i in 걸러야할단어목록:
        가사 = 가사.replace(i,'')
    return 가사

def 공백대체(가사):
    공백으로바꿀목록 = "-\n\t\r"
    for i in 공백으로바꿀목록:
        가사 = 가사.replace(i, ' ')
    return 가사


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

가사빈도수사전 = {}           
for i in 수록곡사전:
    url = f"https://apis.naver.com/vibeWeb/musicapiweb{수록곡사전[i]}/info"
    res = requests.get(url)
    if "<![CDATA[N]]>" in res.text:
        continue
    가사 = res.text.split("<lyric><![CDATA[")[1].split(']]>')[0]
    가사 = 공백대체(가사)
    가사 = 거르자(가사)

    단어목록 = 가사.split()
    for j in set(단어목록):
        if j in 가사빈도수사전:
            가사빈도수사전[j] += 가사.count(j)
        else:
            가사빈도수사전[j] = 가사.count(j)
print(가사빈도수사전)

t.setup(1200,700)
t.hideturtle()
t.shapesize(2)
t.pensize(5)
t.color("red")
t.speed(0)        
t.penup()      

t.colormode(255)
for i in 가사빈도수사전:
    if 가사빈도수사전[i] < 20:
        continue
    t.write(i, font=("맑은고딕", 가사빈도수사전[i]//2, 'bold')) 
    t.goto(r.randint(-500,300), r.randint(-300,150))  
    t.pencolor(r.randint(0,255),r.randint(0,255),r.randint(0,255))   
t.hideturtle()
t.mainloop()