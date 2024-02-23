# N 의 factorial 을 구하는 프로그램

N = int(input("숫자 입력 : "))

gop = 1
for i in range(1, N+1):
    gop *= i
print(N,"! : ",gop)