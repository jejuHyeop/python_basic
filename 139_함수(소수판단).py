# 소수 판단 부분은 풀이2가 이해하기 어렵습니다!!
# 천천히 분석해보세요!!

# 풀이1 : 나는 약수의 개수를 반환하는 걸 함수로 만들래 작전

def 약수의개수반환(N):
    count = 0
    for i in range(1, N+1):
        if N % i == 0:
            count += 1
    return count                  # 자!!! 입력값 반환값을 꼭 잘 생각해서 짜야해요!!!!!!!!!

A = int(input("수를 입력하세요 : "))
A_약수 = 약수의개수반환(A)
if A_약수 == 2:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")



# 풀이2 : 나는 2 에서 N-1 까지 나눠보고 결과에 따라 다른 Bool 값이 반환하도록 할거야!

def 소수판단(N):
    for i in range(2,N):
        if N % i == 0:
            return False
    return True

A = int(input("수를 입력하세요 : "))
if 소수판단(A):
    print("소수입니다.")
else:
    print("소수가 아닙니다.")