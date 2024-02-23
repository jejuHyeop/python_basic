import os
import random
from PIL import Image
import psutil

포켓몬목록 = os.listdir("포켓몬그림자")
정답포켓몬인덱스 = random.randint(0,len(포켓몬목록)-1)
img = Image.open(f"포켓몬그림자/{포켓몬목록[정답포켓몬인덱스]}")


img.show()

# 자 이제 오답 포켓몬 4개를 넣어주겠습니다.
# 나는 정확하게 겹치지 않도록 4개로 뽑을거다!!!
# set 형을 사용하시면 됩니다.
보기인덱스 = set()
보기인덱스.add(정답포켓몬인덱스)
while True:
    if len(보기인덱스) == 5:
        break
    보기인덱스.add(random.randint(0,len(포켓몬목록)-1))
보기인덱스 = list(보기인덱스)
# 어차피 세트형이라 순서가 뒤죽박죽되어있을거에요
# shuffle 해주지 않아도 됩니다.
# 보기인덱스를 list 로바꾸는 이유는
# 정답을 판단할 때 인덱싱을 해주기 위함입니다.


# 사용자에게 물어보기
N = 1
for i in 보기인덱스:
    print(f"{N}.{포켓몬목록[i].split('_')[1].split('.')[0]}")
    N+=1
user = int(input("뭘까요??? 피 피카츄우 ~ "))

# 채점하기
# 이부분을 제일 힘들어하셨어요.
# 결국 사용자는 보기에서 정답을 고를거고, 보기인덱스에는 포켓몬 사진들의 각각의 인덱스가 잇어요
# 사용자가 선택한 숫자는 1~5  보기인덱스는 0~4 잖아요

if 보기인덱스[user-1] == 정답포켓몬인덱스:
    print("맞았습니다.")
    for proc in psutil.process_iter():
        
        if proc.name() in A:
            pass
        else:
            print(proc.name())

else:
    print("틀렸습니다.")

# 만약 여기서 develope 시켜서 많은 문제를 출제하고 싶다.
# 맞추면 img.show 창을 끄고싶다 하시면,
# 검색을 통해 찾아보세요!! 그래도 모르시겠다 하시는 부분은 저에게 연락을 주세요!!
# subprocess 라이브러리 부분이라 라이브러리 학습하시는 연습도 해야죠이제!!
