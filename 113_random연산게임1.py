# 83 번 문제에서 맞추면 점수를 획득하고, 틀리면 라이프가 깎이게 해볼게요

import random 
import os
import time

life = 5
score = 0

while True:

    if life == 0:                               # 반복문 탈출조건 : life 가 0 일 때
        break

    A = random.randint(10,99)
    B = random.randint(10,99)     # 숫자를 뽑는 부분

    print("현재 목숨 :",life,"\t현재점수 :",score)   # 문제 출력전에 현재 목숨과 점수 출력
    print(A,"+",B,"=",end=' ')         # 문제를 출력하는 프로그램

    C = A + B                                  # 문제의 정답을 저장

    user = int(input())                     # 값을 입력받고 정답과 비교해서 판단하는 부분
    if C == user:
        score += 100
        print("맞췄습니다!!")
    else:
        life -= 1
        print("틀렸습니다.")

    time.sleep(1)
    os.system("cls")