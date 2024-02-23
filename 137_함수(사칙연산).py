# 두 수를 입력받고, 사칙연산을 수행하는 프로그램을 작성하세요.
# ※ 사용자에게 사칙연산을 선택할 수 있도록 하세요 !!
#  ex) 더하기 : 1, 빼기 : 2, 곱하기 : 3, 나누기 : 4

def menu():
    print("더하기(1), 빼기(2), 곱하기(3), 나누기(4)")
    A = int(input("메뉴를 선택하세요 : "))
    return A

def add(A,B):
    return A+B    

def sub(A,B):
    return A-B

def mul(A,B):
    return A*B

def div(A,B):
    return A/B         

A = int(input("수를 입력하세요 : "))
B = int(input("수를 입력하세요 : "))

choice = menu()

if choice == 1:
    result = add(A,B)
elif choice == 2:
    result = sub(A,B)
elif choice == 3:
    result = mul(A,B)
elif choice == 4:
    result = div(A,B)
else:
    print("잘못입력되었습니다.")

print("연산결과는 {} 입니다.".format(result))
