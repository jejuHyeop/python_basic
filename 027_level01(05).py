#구입할 사과(3000), 배(2000) 의 개수와 현재 소지
#하고있는 금액을 입력받고,
#구매가 가능할 경우 잔돈이 얼마인지 출력해주고,
#구매가 불가능할 경우 “구매불가” 라고 출력

# 흐름을 제어하는 요소는 소지한 돈과 지불금액의 비교!!!!! 입니다.

사과 = int(input("사과의 개수는?"))
배 = int(input("배의 개수는?"))
돈 = int(input("가지고 있는 돈 : "))

총지불금액 = 사과 * 3000 + 배 * 2000

if 돈 >= 총지불금액: # 만약 돈이 충분할 경우
    print("잔돈은", 돈-총지불금액)
else:
    print("구매불가! 필요한금액 : ", 총지불금액-돈)
    