import os
from PIL import Image

if os.path.isdir('포켓몬250'):
    print("기존의 포켓몬200 폴더를 삭제해주세요")
    exit()
else:
    os.mkdir('포켓몬250')

for i in os.listdir('포켓몬'):
    img = Image.open(f'포켓몬/{i}')
    img = img.resize((250,250))
    img.save(f'포켓몬250/{i}')