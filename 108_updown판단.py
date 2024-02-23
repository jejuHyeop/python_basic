# 하나의 수 랜덤으로 받고, 사용자에게 수를 입력받습니다.
# 사용자의 대답에 따라 Up, Down, Correct!!! 세가지의 상황을 판별하는 프로그램

import random

N = random.randint(10,99)

user = int(input("수를 입력하세요 : "))

if user > N:
    print("Down")
elif user < N:
    print("Up")
else:
    print("Correct!!!")