# 물론, while 또한 for 문 같이 사용할 수는 있습니다!
# 평가를 위한 코딩을 원할경우 말이죠......

# for 문에서 1 에서 5까지 출력
for i in [1,2,3,4,5]:
    print(i)

# while 문에서 1 에서 5까지 출력
i = 1
while i<6:
    print(i)
    i += 1 

# while 로 구구단을 출력하자면... 이렇습니다.

# for 문에서 구구단 출력
for i in range(2,10):
    for j in range(1,10):
        print('{} x {} = {}'.format(i,j,i*j))

# while 문에서 구구단 출력
i = 2
while i < 10:
    j = 1
    while j < 10:
        print('{} x {} = {}'.format(i,j,i*j))
        j += 1
    i+=1

# while 의 경우에는 반복의 지표가 되는 i, j 들을 중간중간 통제해주어야만
# for 를 흉내낼 수 있어요. 그렇기 때문에 대학교 단골문제로 등장하곤하는데..
# 저희는 평가를 위해서 코딩을 하는게 아니잖아요
# 명확히 구분지어서 사용합시다!!

# 실행횟수가 정해져있으면 for!!
# 실행횟수를 모를경우 while!!!