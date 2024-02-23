N = int(input("수 입력 : "))

if N % 400 == 0:
    print("윤년", N)
elif N % 100 == 0:
    pass
elif N % 4 == 0:
    print("윤년", N)
else:
    pass