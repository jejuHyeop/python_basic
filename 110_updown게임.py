# 마찬가지로 80 번 파일에서 게임적인 요소를 넣어볼까요?
# 자, 우선 맞추면 끝나도록 Correct 뒤 부분에 break 를 걸어줍니다.
# 그리고, 몇 번만에 맞췄는지 출력되도록 할게요.
# 몇 번만에 맞추었는가는 어디에 배치하는게 제일 논리적으로 이해하기 쉬울까요?
# 바로!!!! 사용자의 입력이 이루어지면 count 해주는게 제일 논리적이죠?
# 그래서 "수를 입력하세요 : "에서 입력이 이루어질때 해주겠습니다!!

import random
import time
import os

N = random.randint(10,99)

count = 0
# 이부분, 수를 입력받고 위아래 판단하는 부분 부터를 반복하면 되죠?
while True:

    user = int(input("수를 입력하세요 : "))
    count += 1

    if user > N:
        print("Down")
    elif user < N:
        print("Up")
    else:
        print("Correct!!!")
        # 맞추면 반복문이 끝나도록 설정!!
        break
    time.sleep(1)
    os.system("cls")
print(count,"번만에 맞춤")

# 어때요? 조금 게임다워졌나요?