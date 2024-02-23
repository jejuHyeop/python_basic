# 종료를 누를때까지 숫자들의 합을 출력

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
print(sum(li))