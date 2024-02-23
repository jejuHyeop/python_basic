N = int(input("수 입력 : "))

for i in range(1,N+1):
    if i % 2 == 0:
        print(i, "은 짝수 입니다.")
    else:
        print(i,"은 홀수 입니다.")