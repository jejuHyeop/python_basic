# 자! 수업시간에도 다뤘었지만, 이 두 코드의 차이를 보도록 하죠

A = int(input("입력 : "))
B = int(input("입력 : "))

# Program 1 : 공약수를 출력하는 프로그램
if A >= B:
    for i in range(1,B+1):
        if A % i == 0 and B % i == 0:  
            x = i
            print(x)
else:
    for i in range(1,A+1):
        if A % i == 0 and B % i == 0:
            x = i 
            print(x)

# Program 2 : 최대공약수를 출력하는 프로그램
if A >= B:
    for i in range(1,B+1):
        if A % i == 0 and B % i == 0:  
            x = i
else:
    for i in range(1,A+1):
        if A % i == 0 and B % i == 0:
            x = i 
print(x)

# 달라진건 print(x) 의 위치인데요
# 프로그램의 결과는 엄청 다릅니다.
# program 1 의 경우에는 공약수가 모두 출력이되지만
# program 2 의 경우에는 최대공약수를 출력하는 프로그램이 됩니다.

# 그 이유가 무엇일까요?
# 위의 두 개의 프로그램 같은 경우에 x 가 계속 경신되는데요.
# program1 은 x 를 구하고 바로 출력하고 있어요!!!!
# 그렇기 때문에 공약수가 모두 출력되는 것이고!!!!!!!!!!!!!!!!!!!!!!!
# program2 는 x 가 계속 경신이 되는데 출력을 안하고 있다가
# 마지막에 한번 출력하고 있기 때문에 x 에는 자연스럽게 최대공약수만 
# 남겠죠!! (마지막에 저장되는 x 값이 나오기 때문에)
