# 종료를 누를때까지 숫자들을 리스트에 담는것

li = []
while True:
    user = input("그만하려면 q를 누를 입력하세요.") # 문자열을 받아야하니까 int 씌워주면안되죠
    if user == 'q': # q를 입력하면 종료
        print("프로그램을 종료합니다.")
        break
    # 어차피 q를 입력하지 않는 이상 이줄 밑의 코드들이 실행되죠?
    # 그럼? 리스트에 넣어주면 된다구요
    li.append(int(user))
# 그럼 이상 사용자가 숫자를 입력하면 list 에 추가하는 while 문을 끝냈습니다.
print(li)


# 좀 더 정교하게 짜기 위해서는 이렇게 하면좋아요
# 물론 예외처리 파트에서 엄청 세세하게 할 수 있는데요
# 문자열 함수중에 이런게 있어요(미리 말해드릴게요)
# 문자열하고 점을 찍으시고 isnumeric()   > 숫자로 바꿀 수 있는 문자는 True 반환

li = []
while True:
    user = input("그만하려면 q를 누를 입력하세요.") # 문자열을 받아야하니까 int 씌워주면안되죠
    if user == 'q': # q를 입력하면 종료
        print("프로그램을 종료합니다.")
        break
    if user.isnumeric():
        li.append(int(user))
    else:
        print("숫자만 입력하세요!!!!")
# 그럼 이상 사용자가 숫자를 입력하면 list 에 추가하는 while 문을 끝냈습니다.
print(li)
