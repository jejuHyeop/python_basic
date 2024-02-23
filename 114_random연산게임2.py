# 84 번 문제에서 이번에는 다양한 연산 문제가 나오도록 세팅해보겠습니다.

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
    op = random.randint(0,1)        # 두 가지 케이스로 두고 0 이면 덧셈문제 출제, 1이면 뺄셈문제 출제로 설정하겠슴다

    print("현재 목숨 :",life,"\t현재점수 :",score)   # 문제 출력전에 현재 목숨과 점수 출력

    # op 에 따라서 출력하는 문제와 각각의 정답을 바꿔주면 값을 입력받고 판단하는 부분을 수정하지 않아도 된다.

    if op == 0:
        print(A,"+",B,"=",end=' ')         # 덧셈 문제를 출력하는 프로그램
        C = A + B                                  # 덧셈 문제의 정답을 저장
    elif op == 1:
        print(A,"-",B,"=",end=' ')         # 뺄셈 문제를 출력하는 프로그램
        C = A - B                                  # 뺄셈 문제의 정답을 저장

    user = int(input())                     # 값을 입력받고 정답과 비교해서 판단하는 부분
    if C == user:
        score += 100
        print("맞췄습니다!!")
    else:
        life -= 1
        print("틀렸습니다.")

    time.sleep(1)
    os.system("cls")