# 때때로 return 값으로 Bool 값이 활용되기도한다!!

def 짝수판별(N):
    if N % 2 == 0:
        return True
    else:
        return False

N = int(input("수 입력 : "))

if 짝수판별(N):
    print("짝수입니다.")
else:
    print("홀수입니다.")

