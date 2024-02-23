import os
from bs4 import BeautifulSoup
import requests

if os.path.isdir('포켓몬'):
    print("기존의 포켓몬 폴더를 삭제해주세요")
    exit()
else:
    os.mkdir('포켓몬')

res = requests.get("http://pokemongo.inven.co.kr/dataninfo/pokemon/")
soup = BeautifulSoup(res.text,"html.parser")

for i in soup.select(".pokemonicon"):
    포켓몬경로 = i.select_one("img").get('src')
    포켓몬이름 = i.select_one(".pokemonname").text
    print(포켓몬경로, 포켓몬이름)
    res = requests.get("https:"+포켓몬경로)
    f = open(f"포켓몬/{포켓몬이름}.png", "wb")
    f.write(res.content)
    f.close()

