# 시간과 분을 입력받고, N분 후 시간을 출력해주는 프로그램

시간 = int(input("시간 :"))
분 = int(input("분 :"))
N = int(input("N 분전 :"))

총분 = 시간 * 60 + 분 + (N%1440)
if 총분 >= 1440:
    총분 -= 1440
print(N,"분 후 : ",총분//60,"시",총분%60,"분")

