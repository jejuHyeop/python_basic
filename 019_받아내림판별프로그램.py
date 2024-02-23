# 두 수를 입력받고(0-99), 큰 수에서 작은 수를 뺏을 때
# 받아내림이 발생하는지 판별하는 프로그램을 작성하세요.

# 자, 받아올림과 다른점은, 큰 수!!! 에서 작은 수 !!! 를 빼야한다는
# 추가적인 조건이 있습니다!!

A = int(input("첫번째 수 입력 : "))
B = int(input("두번째 수 입력 : "))

A_tail = A % 10  
B_tail = B % 10
# 여기서 A 가 B 보다 클 경우, A_tail - B_tail 를
# B 가 A 보다 클 경우, B_tail - A_tail 를 해야합니다.
# 따라서 다음과 같은 조건이 선행되고, 받아내림을 판별해야 합니다.

if A > B:
    if A_tail - B_tail < 0:
        print("받아내림이 발생합니다.")
    if A_tail - B_tail >= 0:
        print("받아내림이 발생하지 않습니다.")

if B > A:
    if B_tail - A_tail < 0:
        print("받아내림이 발생합니다.")
    if B_tail - A_tail >= 0:
        print("받아내림이 발생하지 않습니다.")

