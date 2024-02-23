# 랜덤으로 뽑은 수 A, B 의 덧셈을 맞추는 프로그램을 작성하세요

import random 

A = random.randint(10,99)
B = random.randint(10,99)     # 숫자를 뽑는 부분

print(A,"+",B,"=",end=' ')         # 문제를 출력하는 프로그램

C = A + B                                  # 문제의 정답을 저장

user = int(input())                     # 값을 입력받고 정답과 비교해서 판단하는 부분
if C == user:
    print("맞췄습니다!!")
else:
    print("틀렸습니다.")