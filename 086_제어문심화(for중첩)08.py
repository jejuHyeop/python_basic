# 단별로 구구단 출력

for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)

# 여기서 추가 요청!!
# 단이 출력되기전에 N단이 출력됩니다 라고 하고
# 단 출력후에 한칸 띄워주기!!
# 엄청 쉬워요 기능나누기 발동!

for i in range(2,10):
    for j in range(1,10):
        print(i,"X",j,"=",i*j)   

# 12 번 코드는 단을 바꾸는 코드 자나요
# 13, 14 번 코드는 해당 구구단을 출력하는 코드
# 그럼 구구단을 출력하는 13-14 전후로 뭐 하면되죠?????

# 단이 출력되기전에 N단이 출력됩니다 라고 하고
# 단 출력후에 한칸 띄워주기!!
# 이거하면되죠

for i in range(2,10):
    print(i,"단")
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print()   