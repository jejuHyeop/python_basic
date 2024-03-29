# 함수에서 중요한건
# 입력되는 값, 반환되는 값을 먼저 생각하고 코딩하는 것!!
# 기본형식은
# def 함수의이름(입력값1, 입력값2, ... ):
#     함수의 내용
#     return 반환값1, 반환값2, ...

# 만약 두 수의 합을 반환하는 함수를 만든다고 가정해볼게요!
# 입력값은 두 수!! 일 것이며, 반환되는 값은 합!! 이잖아요?
# 아래와 같이 함수를 만들 수 있을 거에요
def add1(A, B):           # A,B 를 입력받는 add 라는 함수를 선언
    return A+B           # A+B 가 반환되도록 한다.

# 그럼, 이제 사용은 어떻게 할까?
# 반환!! 이라는 개념을 재차 강조해왔어요!
# add(A,B) 라는 표현이 반환값인 A+B 로 바뀐다는거!!! 그게 반환이라는거!!!!
# 이거 놓치시면 안됩니다!!!

# 만약 두 수를 입력받고, 두 수의 합을 출력하는 프로그래밍을 하여라(함수사용)

def add2(A,B):
    return A+B

C = int(input("수 입력 : "))
D = int(input("수 입력 : "))

add2(C,D)
# 이렇게 코딩하면 안되겠죠!!! 왜냐하면 출력이 안되기 때문이에요!!
# 하려면 어떻게 해요?

# 방법 1
def add3(A,B):
    return A+B

C = int(input("수 입력 : "))
D = int(input("수 입력 : "))

print(add3(C,D))         # 반환되는 값을 바로 출력해주거나

# 방법 2
def add4(A,B):
    return A+B

C = int(input("수 입력 : "))
D = int(input("수 입력 : "))

F = add4(C,D)          # 반환되는 값을 저장할 변수를 만들어 주거나
print(F)

# 방법 3
def add5(A,B):           # 함수를 수정하거나
    print(A+B)

C = int(input("수 입력 : "))
D = int(input("수 입력 : "))

add5(C,D)          

