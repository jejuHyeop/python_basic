# bool 값을 반환!!!! 하는 또 다른 연산자를 볼 것입니다.
# 논리연산자 입니다!! 논리연산자는 [ ★ Bool 값 끼리의 연산 ] 을 합니다!!!
# 대표적으로 and 와 or 이 있습니다. 

print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False
# and 는 둘다 True 일 경우 True 를 반환합니다!!!!

print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False
# or 는 둘 중 하나라도 True 일 경우 True 를 반환합니다!!!!

print(not True)
print(not False)

''' 

여기서 중요한 사실은!!!
비교연산자가 bool 값을 반환했습니다. 논리연산자는 bool 값끼리의 연산을 하지요.
따라서 아래와 같은 형태로 자주 사용됩니다.

ex1)  A 가 10보다 크다 그리고 20 보다 작다!!
      A > 10   and    A < 20    
      -----           ------ 
      bool값   and    bool값

'''

A = 30

print( A>10 and A < 20 )
print( A>10 or A < 20 )
print(not A>10  and not A>10)

# if 비교연산자 and 비교연산자:
# if 비교연산자 or 비교연산자:










