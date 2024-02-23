# 5 개의 점수를 입력받고 평균보다 낮은 수들을 구하는 프로그램

li = []
for i in range(5):
    N =int(input("입력 : "))
    li.append(N)

평균 = sum(li)/len(li)
print("평균은",평균)
# 자 리스트로 하니까 평균하고 각각의 수를 비교할 수 있는거에요
# 이제 각각의 자료에 접근을 해야되네요! 
# for!!

for i in li:
    if i <= 평균:
        print(i, "는 평균이하")


