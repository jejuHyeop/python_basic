# 자!! 이번에는 반복 범위가 숨어있는 문제중
# 가장 대표적인 문제 약수 문제를 볼건데요

# 언핏보기에 약수라는 것을 구할 때
# 반복문이 필요하다는 생각을 하기 힘드실 수도 있는데
# 약수를 모두 알아보기 위해서
# 어떤 수 N 을 대상으로 1 ~ N 으로 일일히 나눈 나머지를 조사해봐야하기
# 때문에 반복문이 필요한 것입니다.

# 만약 6의 약수를 구하려면
# 6이랑 1을 나눠서 나누어떨어지냐?
# 6이랑 2을 나눠서 나누어떨어지냐?
# 6이랑 3을 나눠서 나누어떨어지냐?
# 6이랑 4을 나눠서 나누어떨어지냐?
# 6이랑 5을 나눠서 나누어떨어지냐?
# 6이랑 6을 나눠서 나누어떨어지냐?
# 검사를 해야합니다.

# 자, 그럼 약수 문제를 풀어볼까요?

# N 을 입력받고, N 의 약수를 출력하는 프로그램
N = int(input("입력 :"))

for i in range(1,N+1):       # 1 ~ N 까지 i 가 접근하게 되겠네요
    if N % i == 0:                # N 을 1~N 으로 나눴을 때 나눠 떨어지면 ( = 약수라면 )
        print(i)                        # 출력하면되죠!




