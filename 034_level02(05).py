# 오늘은 화요일이다. N 일 후에는 무슨 요일일까?
# 3,4 번 문제와 다르지 않아요
# 아무리 큰 N 도 월화수목금토일안에 들어가도록 해야겠죠?
# %7 이 핵심입니다. %7 하고 매칭만 시켜주면되요!

N = int(input("몇 일후?"))

if N % 7 == 1:
    print("수요일")
elif N % 7 == 2:
    print("목요일")
elif N % 7 == 3:
    print("금요일")
elif N % 7 == 4:
    print("토요일")
elif N % 7 == 5:
    print("일요일")
elif N % 7 == 6:
    print("월요일")
else:
    print("화요일")
        
    