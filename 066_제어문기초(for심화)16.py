# 두 수(A,B)를 입력 받고 받아올림을 판별하는 프로그램

A = int(input("수 입력 : "))
B = int(input("수 입력 : "))

if A % 10 + B % 10 > 9:
    print("받아올림 발생 O")
else:
    print("받아올림 발생 X")