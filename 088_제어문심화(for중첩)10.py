# N 을 입력받고 N이 소수인지 판별하는 프로그램

N = int(input("수 입력 : "))

# 리스트로 처리하겠습니다!
# 약수 개수 len(li) 만 구하면 되는 거자나요
li = []
for i in range(1, N+1):
    if N % i == 0:
        li.append(i)
if len(li) == 2:
    print(N,"은 소수입니다.")
