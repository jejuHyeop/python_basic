# 번역기를 돌리는 프로그램인데요
# 어떤분은 네이버에서부터 파파고를 입력하고 접근하는 방식으로했는데
# 안된다고 하더라구요!
# 찾아보니 파파고를 누를때 창이 추가적으로 생겨서 제대로 동작하지 않았던 거였습니다.
# 그래서, 창을 옮겨주어야해요!

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.naver.com")
sleep(2)

검색창 = driver.find_element_by_css_selector("#query")
검색창.send_keys("파파고")
sleep(2)
검색버튼 = driver.find_element_by_css_selector(".btn_submit")
검색버튼.click()

파파고 = driver.find_element_by_css_selector('.link_name')
파파고.click()
sleep(3)

# 이부분이 새창으로 기준을 옮겨주는 역할을 합니다
driver.switch_to_window(driver.window_handles[1])

파파고검색 = driver.find_element_by_css_selector("#txtSource")
파파고검색.send_keys("apple")
sleep(10)
driver.close()