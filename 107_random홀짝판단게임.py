# 77번 파일에서 이번에는 게임적인 요소들을 넣어볼까요?

import random    
import os
import time

# 강사님 저는 life 를 5 개 주고 틀릴때마다 -1 해주고싶어요.
# life 가 0이면 프로그램이 종료되도록 하고싶습니다. 그럼 그냥 틀렸습니다 프린트 위에 life -= 1 해주면 되겠네요

life = 5
score = 0
# 저는 홀 짝을 맞추면 점수를 +100 점 하도록 해줄래요.
# 그럼 score 라는 변수를 만들고 맞출때마다 +100 해주면 되겠네요

while True:
    if life == 0:
        print("Game Over")
        break
    N = random.randint(10,99)
    print("현재 목숨", life,"현재 점수",score)
    user = int(input("input 홀(0), 짝(1) : "))

    if N % 2 == 0:
        if user == 0:
            life -= 1
            print("틀렸습니다.")
        else:
            score += 100
            print("맞았습니다.")
    else:
        if user == 0:
            score += 100
            print("맞았습니다.")
        else:
            life -= 1
            print("틀렸습니다.")   

    print("컴퓨터의 숫자는",N,"이었습니다.")
    print()
    time.sleep(1)
    os.system('cls')

print("총 점수 :",score)