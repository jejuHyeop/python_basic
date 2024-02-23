# 약수개수를 세주는 함수를 만들거에요!!
# 자!! 이거만 기억합시다
# 1. 묶고싶은기능
# 2. 입력값
# 3. 반환값

# 1. 기능 : 약수 개수를 세는것
# 2. 입력값 : 약수의 개수를 판단할 대상
# 3. 반환값 : 약수의 개수

def 약수개수(X):                  
    return 약수의개수            # 이렇게 출발합니다!!!
                                            # 우선 함수의 모양을 잡아놓고!!!!!
                                            # 그 안에 기능을 구현하면되요!!!!
                                            # 11,12 번째 라인은 완벽하게 구성했으니!!!!!
                                            # 이제 더이상 짜줄게 없습니다!!!!!!!!!!
                                            # 그다음에 코드를 어떻게 짤지 고민!!!
                                            # X 하나만 가지고 약수의 개수를 구해야겠다!!
                                            # X 를 입력받고, X 의 약수의 개수를 구하는건 앞단원에서 했었어요!!!!!
                                            # 그 상황이라고 생각하시면 됩니다

def 약수개수(X):
    약수의개수 = 0
    for i in range(1,X+1):
        if X % i == 0:
            약수의개수 += 1
    return 약수의개수         

# 리스트의 길이로 반환하는 것도 가능하겠죠?
def 약수개수(X):
    약수의개수 = []
    for i in range(1,X+1):
        if X % i == 0:
            약수의개수.append(i)
    return len(약수의개수)                                          




# 이번에는 함수에서 약수들을 반환하도록 해볼게요
# 함수에서 return 을 만나는 순간 함수가 끝나기 때문에
# list 로 만들어서 넘겨주어야해요!!

# 자!! 이거만 기억합시다
# 1. 묶고싶은기능
# 2. 입력값
# 3. 반환값

# 1. 묶고싶은 기능 : 약수를 반환하는것
# 2. 입력값 : 약수 판단 대상 (A)
# 3. 반환값 : 약수

# 자, 이상태에서 구도만 잡아볼까요
def 약수반환(A):
    return 약수리스트               # 그럼 이제 기능구현만 남았어요.
                                               # 15, 16 번째줄은 건들면 안되는 코드입니다!!!!

def 약수반환(A):
    약수리스트 = []
    for i in range(1,A+1):
        if A % i == 0:
            약수리스트.append(i)
    return 약수리스트













# 자!! 이거만 기억합시다
# 1. 묶고싶은기능
# 2. 입력값
# 3. 반환값

# Q. 수를 입력받고, 소수와 완전수의 여부를 판단하는 프로그램
# 둘다 약수에 관한 내용입니다~~ 그래서 약수를 뽑아오는 함수를 만들어주자구요!!
# 1. 묶고싶은 기능 : 약수를 리스트로 반환해주고싶음
# 2. 입력값 : 약수를 뽑을대상 (A)
# 3. 반환값 : 약수를 리스트 형태로 반환!!!!!

def 약수뽑기(X):     
    li = []
    for i in range(1,X+1):
        if X % i == 0:
            li.append(i)
    return li

A = int(input("수를 입력하세요 : "))
약수리스트 = 약수뽑기(A)
if len(약수리스트) == 2:
    print("소수입니다.")
else:
    print("소수가 아닙니다.")

if sum(약수리스트[:-1]) == A:       # 리스트 마지막요소(자기자신) 전까지의 값을 sum 해줌! 
    print("완전수입니다.")
else:
    print("완전수가 아닙니다.")
