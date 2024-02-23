# 86 문제에서 이번에는 난이도 조정부분을 해볼게요
# 1. 쉬움 2. 노멀 3.어려움으로 나눠보려고해요
# 쉬움은 한자리 수 끼리의 연산, 노멀은 두자리 수 끼리의 연산, 어려움은 세자리수의 연산입니다.
# 난이도는 게임전 한번만 설정하는 걸로 하겠습니다.

import random 
import os
import time

life = 5
score = 0

난이도 = int(input("난이도 하(1), 난이도 중(2), 난이도 상(3) 선택 : "))

while True:

    if life <= 0:                               # 만약 라이프가 1인데 2 가 깎이면 이부분을 처리해줘야함!!!!!!!!!!!!!!!!!!!!!!!!
        break                                     # life == 0 을 하게되면 -1이 되는순간 무한반복이됨.

    if 난이도 == 1:
        A = random.randint(1,9)
        B = random.randint(1,9)     
    elif 난이도 == 2:
        A = random.randint(10,99)
        B = random.randint(10,99) 
    else:
        A = random.randint(100,999)
        B = random.randint(100,999) 

    op = random.randint(0,1)        # 두 가지 케이스로 두고 0 이면 덧셈문제 출제, 1이면 뺄셈문제 출제로 설정하겠슴다
    s200 = random.randint(1,5)   # 1~5 중에 하나만 설정하면 1/5 확률이됨
    l2 = random.randint(1,4)        # 1~4 중에 하나만 설정하면 1/4 확률이됨

    print("현재 목숨 :",life,"\t현재점수 :",score)   # 문제 출력전에 현재 목숨과 점수 출력

    if s200 == 1:       # 1 이 나오면 200 점 짜리 문제라고 설정
        print("자 이문제는 200점 짜리 문제입니다.")
        점수 = 200
    else:                   # 여기서 else 를 해준이유 : 만약 200 점 문제가 출제되고 나면 계속 200점이 되는거 방지
        점수 = 100

    if l2 == 1:
        print("자 이문제는 라이프가 2개 걸린 문제입니다.")
        라이프 = 2
    else:
        라이프 = 1

    if op == 0:
        print(A,"+",B,"=",end=' ')         # 덧셈 문제를 출력하는 프로그램
        C = A + B                                  # 덧셈 문제의 정답을 저장
    elif op == 1:
        print(A,"-",B,"=",end=' ')         # 뺄셈 문제를 출력하는 프로그램
        C = A - B                                  # 뺄셈 문제의 정답을 저장

    user = int(input())                     # 값을 입력받고 정답과 비교해서 판단하는 부분
    if C == user:
        score += 점수
        print("맞췄습니다!!")
    else:
        life -= 라이프
        print("틀렸습니다.")

    time.sleep(1)
    os.system("cls")