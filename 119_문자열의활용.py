# 문자열 또한 순서있는 자료형이였어요!!
# 순서가 있다는 의미는
# 1. index 개념이 존재한다.
# 2. for 문에서 활용이 가능하다. 
# 두 개의 의의를 가지고있죠!

hello = 'hello world'
print(hello[0])
print(hello[4])
# index 값에는 마이너스 값도 있어요!!(있다고만 아셔도되요)
# 마이너스 값에 len(a)를 더해서 생각하시면되요. 리스트 자료의 개수
# 만약 a = [1,2,3] 이면 len(a) = 3 이므로
# a[-1] = a[2] = 3
# a[-3] = a[0] = 1

for i in hello:
    print(i)
