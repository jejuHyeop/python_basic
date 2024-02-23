# 이번에는 수록곡 모음이에요
# 수록곡페이지를 열어보았을 때
# requests? selenium? 
# 어떤걸 써야겠어요???

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

# 여기까지는 161 번 파일입니다.
# 이제 앨범 각각의 경로로 이동해서 수록곡을 뽑아서 
# 딕셔너리 형으로 저장해볼거에요


# 여기부터 중요하죠! dictionary 를 for 문으로 처리하면 
# 키값이 i 에 담긴다는 사실!! 
# 이제 각각의 경로!! 에 접근해야하니
# driver.get(  ) 여기 괄호 값을 유의해서 넣어주어야하죠?
앨범수록곡 = {}  # key  : 앨범제목      value : 수록곡들!!! ( 리스트에요 밸류가!! )
for i in 앨범사전:
    driver.get(앨범사전[i])
    sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, "lxml")
    앨범수록곡[i] = []                      # 이부분 잘처리해주셔야해요!!!
    for j in soup.select('.inner_cell > a'):
        #print(j.text)  # 확인!!
        수록곡제목 = j.text
        앨범수록곡[i].append(수록곡제목)
print(앨범수록곡)
# 확인!!



