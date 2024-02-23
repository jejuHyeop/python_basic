# 종료를 누를때까지 숫자들의 평균, 그 이상인 숫자들 출력

li = []
while True:
    user = input("그만하려면 q를 누를 입력하세요.") 
    if user == 'q': 
        print("프로그램을 종료합니다.")
        break
    li.append(int(user))
# 기능 분리가 이렇게 중요하답니다.
# 56 번 파일에서 위의 코드 손볼게 있을까요?
# 없어요

avg = sum(li) / len(li)

# 여기 까지는 59 번파일과 같습니다.
# 이제 각각의 자료들과 평균을 비교하면 되겠네요.
# 각각의 자료에 접근하는 문법 For 입니다!!!!!
# for 처음배울 때, 리스트로 접근했던 거 기억나시죠

for i in li:
    if i >= avg:
        print(i)
