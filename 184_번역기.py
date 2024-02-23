from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://papago.naver.com/")

sleep(1)

f = open("news.txt","r",encoding="utf-8")
h = open("inter_news.txt","w",encoding="utf-8")

for i in f.readlines():
    
    번역전 = driver.find_element_by_css_selector('#txtSource')
    번역전.send_keys(i)
    sleep(2)
    번역후 = driver.find_element_by_css_selector('#txtTarget')
    h.write(번역후.text+"\n")
    
    remo = driver.find_element_by_css_selector('#sourceEditArea > button')
    remo.click()

h.close()
f.close()


    