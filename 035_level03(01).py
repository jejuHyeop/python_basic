# 큰 수에서 작은 수를 뺐을 때, 받아내림이 발생하는지 판별하는 프로그램
# 가정!! 두자리수!

A = int(input("수 입력 :"))
B = int(input("수 입력 :"))

# 우선 어디에서 어디로 빼는지는 A, B 대소비교를 통해서 결정되기 때문에!!!
# 대소 판별먼저 우선이 되야해요!!!
# 물론 계산을 먼저해도되지만, 불필요해질 계산은 하지 않는게 좋겠죠?
A일의자리 = A % 10
B일의자리 = B % 10

if A > B: # 이경우는 A 에서 B 를 빼야함
    # 그 다음으로 내림이 발생하는지 체크해야합니다.
    if B일의자리 > A일의자리:
        print("받아내림 발생")
    else:
        print("받아내림 안발생")
else:
    if A일의자리 > B일의자리:
        print("받아내림 발생")
    else:
        print("받아내림 안발생")
