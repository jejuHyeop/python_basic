# 또 다른 차이는 코드의 의미 차원의 차이점입니다.

score = 84

if score > 90:
    print("A")
if score > 80:
    print("B")
if score > 70:
    print("C")
if score <=70:
    print("F")
# 위의 코드의 출력결과 'BC' 가 출력됩니다!!!

if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
else:
    print("F")
# 위의 코드의 출력결과 'B'가 출력됩니다!!

# 별다른 설명없이 출력결과를 이해해보시길 바랍니다.
# 만약 위의 코드를 if 로만 프로그래밍한다면
if score > 90:
    print("A")
if score > 80 and score <= 90:
    print("B")
if score > 70 and score <= 80:
    print("C")
if score <=70:
    print("F")
# 다음과 같이 코딩해야할 것 입니다.