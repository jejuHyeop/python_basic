# 자, 우선 N 을 랜덤으로 받고, 사용자에게 "홀","짝" 을 입력받은뒤,
# 사용자가 맞았는지, 틀렸는지 구분하는 프로그램을 작성해볼까요?

import random    # 이 구문이 있어야 randint 를 사용할 수 있어요!!

N = random.randint(10,99)
user = int(input("input 홀(0), 짝(1) : "))

if N % 2 == 0:
    if user == 0:
        print("틀렸습니다.")
    else:
        print("맞았습니다.")
else:
    if user == 0:
        print("맞았습니다.")
    else:
        print("틀렸습니다.")   

print("컴퓨터의 숫자는",N,"이었습니다.")

