N = int(input("수 입력 : "))

if N % 4 == 1:
    print(N, "당번 A")
if N % 4 == 2:
    print(N, "당번 B")
if N % 4 == 3:
    print(N, "당번 C")
if N % 4 == 0:
    print(N, "당번 D")
