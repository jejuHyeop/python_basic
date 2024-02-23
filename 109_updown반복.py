# 마찬가지로 79 번 파일을 반복하는 프로그램!! 그냥 따오세요~
# 자, 여기서 중요한거 랜덤으로 받아오는 수를 이번에는 while True 에 넣어주면 안되겠죠?
# 왜냐하면 up down 게임 특성상 기준이 되는 수를 바꾸면 안되요
# 맞추잖아요? 돗자리 피셔야합니다.

import random
import time
import os

N = random.randint(10,99)

# 이부분, 수를 입력받고 위아래 판단하는 부분 부터를 반복하면 되죠?
while True:
    user = int(input("수를 입력하세요 : "))

    if user > N:
        print("Down")
    elif user < N:
        print("Up")
    else:
        print("Correct!!!")
        