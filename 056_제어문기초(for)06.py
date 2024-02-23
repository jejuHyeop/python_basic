N = int(input("수 입력 : "))

li = []
for i in range(1, N+1):
    if i % 2 == 1:
        li.append(i)
print(li)