# 82 번 문제를 반복해볼게요.
# 만약 컴퓨터가 낸 문제를 고정적으로 가지고 가고 싶다면 6,7 을 반복하면 안되고,
# 컴퓨터가 낸 문제를 계속적으로 바꾸고 싶다면 전부~~~ 반복해야죠


import random 

while True:
    A = random.randint(10,99)
    B = random.randint(10,99)     # 숫자를 뽑는 부분

    print(A,"+",B,"=",end=' ')         # 문제를 출력하는 프로그램

    C = A + B                                  # 문제의 정답을 저장

    user = int(input())                     # 값을 입력받고 정답과 비교해서 판단하는 부분
    if C == user:
        print("맞췄습니다!!")
    else:
        print("틀렸습니다.")