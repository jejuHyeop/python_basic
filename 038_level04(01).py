# 시간과 분을 입력받고, N분 전 시간을 출력해주는 프로그램
# 자!! 이문제 어떻게 바라보아야하냐!
# 아무리 큰 수도 내가 원하는 것으로 만들어버리는 거에요!!!
# N 이 아무리 커도 하루 안의 시간으로 해석되도록 하려면 
# % 1440 하면 되요!
# level03 의 문제 풀이와 나머지는 동일해요!

시간 = int(input("시간 :"))
분 = int(input("분 :"))
N = int(input("N 분전 :"))

총분 = 시간 * 60 + 분 - (N%1440)
if 총분 < 0:
    총분 += 1440
print(N,"분 전 : ",총분//60,"시",총분%60,"분")

