# 1부터 10까지의 합을 구하여라

su = 0
for i in range(1,11):
    su += i
print(su)

'''
 첫 번째 반복 때, su = su + 1            
 두 번째 반복 때, su = (su + 1) + 2
 세 번째 반복 때, su = (su + 1 + 2) + 3
 ...
 열 번째 반복 때, su = (su + 1 + 2 + 3 + 4 + 5 + 6 + ... + 9) + 10      
'''
# 여기서 중요한 것은 computer 는 su 라는 값이 무슨 값인지 모르기
# 때문에 su 값을 설정해주어야하는데 덧셈에서 아무런 지장 없는 수는
# 0 이기 때문에 su = 0 이라는 구문을 넣어주어야한다!!



# 1 에서 100 까지의 합!!
su = 0
for i in range(1,101):
    su += i
print(su)

# 1 에서 입력받은 N 까지의 합!!
N = int(input("수 입력 "))
su = 0
for i in range(1,N+1):
    su += i
print(su)
