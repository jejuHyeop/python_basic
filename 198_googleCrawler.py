# 이친구는 base64 저장방식으로 사진을 저장하고 있습니다!!
# 이부분은 다른 수업에서 들을 수 있을 거에요!!

# 간단하게 사진 바이너리값이 base64 라는 인코딩 기법으로 저장되어 있다는 것인데요
# 이부분 한번 공부해주세요!!

import requests
from bs4 import BeautifulSoup
import os
from time import sleep
import base64
from selenium import webdriver

keyword = input("뭐 검색할까요 ? ")


if os.path.isdir(keyword):
    print("이미 존재하는 폴더")
else:
    os.mkdir(keyword)

driver = webdriver.Chrome("chromedriver.exe")
url = f"https://www.google.co.kr/search?q={keyword}&sxsrf=ALeKk00dRlgPHiqz_k49BCia6vOrE7MUPA:1619833884996&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjDtr26r6fwAhWt-GEKHZysDU8Q_AUoAXoECAEQAw&biw=1600&bih=810"
driver.get(url)
sleep(2)
page = driver.page_source
soup = BeautifulSoup(page, "lxml")

for num, i in enumerate(soup.select('img.Q4LuWd'),1):
    if i.get('src') == None:
        continue
    re = i.get('src').split('/jpeg;base64,')[1]
    h = open(f"{keyword}/{keyword}{num}.png", "wb")
    h.write(base64.b64decode(re))
    h.close()