from selenium import webdriver
from time import sleep
import requests
import os
from bs4 import BeautifulSoup

keyword = input("검색어 입력 : ")

if os.path.isdir(keyword):
    print("이미 존재하는 폴더입니다. 폴더를 삭제해주세요 ")
    exit()
else:
    os.mkdir(keyword)

driver = webdriver.Chrome("chromedriver.exe")
driver.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}")
sleep(4)

for i in range(5):
    driver.execute_script(f"scrollTo(0,{i*300})")
    sleep(2)

page = driver.page_source
soup = BeautifulSoup(page, "lxml")

for num, i in enumerate(soup.select("._listImage"),1):
    if len(i.get('src')) < 100:
        continue
    res = requests.get(i.get('src'))
    f = open(f"{keyword}/{keyword}{num}.png","wb")
    f.write(res.content)
    f.close()