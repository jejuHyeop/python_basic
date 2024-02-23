import requests
import os
from bs4 import BeautifulSoup

if os.path.isdir("lolcharacter"):
    pass
else:
    os.mkdir("lolcharacter")

res = requests.get("http://lol.inven.co.kr/dataninfo/champion/")
soup = BeautifulSoup(res.text,"html.parser")

for i in soup.select("div.champImage > a"):
    캐릭터이름 = i.get('title').split("(")[0]
    캐릭터src = i.select('img')[0].get('src')
    f = open(f"lolcharacter/{캐릭터이름}.png","wb")
    re = requests.get("http:"+캐릭터src)
    f.write(re.content)
    f.close()

