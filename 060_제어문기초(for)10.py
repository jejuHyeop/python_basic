N = int(input("수 입력 : "))

for i in range(1,N+1)
    if i % 4 == 1:
        print(i, "당번 A")
    if i % 4 == 2:
        print(i, "당번 B")
    if i % 4 == 3:
        print(i, "당번 C")
    if i % 4 == 0:
        print(i, "당번 D")