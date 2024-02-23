N = int(input("수 입력 : "))

for i in range(1, N+1): 
    if i % 400 == 0:
        print("윤년", i)
    elif i % 100 == 0:
        pass
    elif i % 4 == 0:
        print("윤년", i)
    else:
        pass