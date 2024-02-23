import os
from PIL import Image

if os.path.isdir('포켓몬그림자'):
    print("기존의 포켓몬그림자 폴더를 삭제해주세요")
    exit()
else:
    os.mkdir('포켓몬그림자')

for i in os.listdir("포켓몬250"):
    img = Image.open(f"포켓몬250/{i}")
    
    for j in range(img.size[0]):
        for k in range(img.size[1]):
            rgb = img.getpixel((j,k))
            if rgb != (0,0,0,0) and rgb[3] > 10:
                img.putpixel((j,k), (0,0,0,255))
    
    img.save(f"포켓몬그림자/{i}")

