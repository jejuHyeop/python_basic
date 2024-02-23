# 수업시간에 했던 메뉴판 프로그램입니다.
# 한번 작성하고 나면 감이 생기실 거에요
# 사용자의 메뉴 선택에 따라서 프로그램의 반복 순서가 결정되요!!!
# 그래서 반복횟수가 정해지지 않은 while 을 사용해야합니다.

# 반복 하건 뭐냐면요!!
# 우선 기획을 해보세요!!

# 기획1     -   기획 2             -  기획3
# 메뉴 출력 - 사용자 선택 - 선택에 따른 처리

# while True:
#    메뉴출력및현재금액출력및선택받음()
#    선택에따른처리()

# 이게 끝이에요. 이걸 while True 해주면 되요 ㅎㅎ

money = 0
while True:
    
    print("="*20)
    print("1. 콜라 / 300")
    print("2. 사이다 / 300")
    print("3. 커피 / 200")
    print("4. 돈 입력")
    print("5. 잔돈반환")
    print("6. 종료")
    print("="*20)
    print("현재 금액",money)
    
    메뉴 = int(input("메뉴를 입력해주세요 : "))

    if 메뉴 == 1:
        money = 일번메뉴(money)
    elif 메뉴 == 2:
        if money < 300:
            print("금액이 부족합니다.")
        else:
            print("사이다 맛있게 드세요.")
            money -= 300
    elif 메뉴 == 3:
        if money < 200:
            print("금액이 부족합니다.")
        else:
            print("커피 맛있게 드세요.")
            money -= 200
    elif 메뉴 == 4:
        m = int(input("돈을 넣어주세요 :"))
        money += m
    elif 메뉴 == 5:
        print("잔돈이 반환 됩니다.")
        money = 0
    elif 메뉴 == 6:
        break
    else:
        print("잘못 입력하셨습니다.")