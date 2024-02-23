# X, Y 를 입력받고 둘중 큰수를 출력하세요.
# 함수1. 나는!! 큰수가 return 되도록 할거야
# 함수2. 나는!! 그냥 함수딴에서 print 되도록 할래

def 함수1(A, B):
    if A >= B:
        return A
    else:
        return B

def 함수2(A, B):
    if A >= B:
        print(f"{A}가 크다")
    else:
        print(f"{B}가 크다")

X = int(input("수 입력 : "))
Y = int(input("수 입력 : "))
# 자 여기서 잘생각!! 함수1 은 반환값이 있고,
# 2 는 없습니다.
# 함수1로 풀이!!!!
max_XY = 함수1(X,Y)
print(f"{max_XY}가 더 크다.")
# 함수2로 풀이!!!
함수2(X,Y)
# 반환값이 없고, 함수딴에서 처리되도록 했으니~~~!!! 이것만 해줘도됨



