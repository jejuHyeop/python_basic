# N 을 입력받고 N의 약수를 구하는 프로그램

N = int(input("수 입력 : "))

for i in range(1,N+1):
    if N % i == 0:
        print(i)