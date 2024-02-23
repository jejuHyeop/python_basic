# 5 개의 점수를 입력받고 평균을 구하는 프로그램
# 평균 구할때 리스트로 그냥하는게 편합니다~

li = []

for i in range(5):
    N = int(input("점수입력 : "))
    li.append(N)
평균 = sum(li)/len(li)

print("평균은", 평균)