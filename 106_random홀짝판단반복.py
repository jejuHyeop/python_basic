# 76번 파일을 그대로 긁어서 옵니다.
import random    

# 하나의 random 한 수를 홀짝판단하는 코드였죠?
# 이 전체를 반복하면 어떻게 될까요? 그냥 while True 하시고 전체를 들여쓰기 하세요.
# 코드하나도 손대지 마시고
# 그럼 계속적으로 랜덤한 수가 홀수인지 짝수인지 맞추는 프로그램이 되겠죠?
while True:
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

