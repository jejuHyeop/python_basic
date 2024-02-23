# 1~N 의 factorial 을 구하는 프로그램

N = int(input("숫자 입력 : "))

for i in range(1,N+1):
    gop = 1    # 대상마다 곱을 저장할거기 때문에 계속 1로 초기화가 이뤄져야죠!
    for j in range(1, i+1):
        gop *= j
    print(i,"! : ",gop)

# 즉, i, j 가 무엇이냐에 대한 개념만 남아있으면 
# 코드를 해석하기 쉬울것입니다.

# i : 대상
# j : 곱할범위