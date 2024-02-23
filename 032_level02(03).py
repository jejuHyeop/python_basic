#생년월일을 입력받고, 무슨 띠인지 출력하는 프로그램
# 자축인묘진사오미신유술해 (쥐,소,호랑이,토끼,용,뱀,말,양,원숭이,닭,개,돼지)

birth = int(input("생년월일 입력 :"))

# 아무리~~~ 큰 년도도 12 가지 상황에서 돌아야하죠!
# 이게 % 연산자를 사용하는 Signal 입니다!

index = birth // 10000 % 12

if index == 1:
    print("닭")
elif index == 2:
    print("개띠")
elif index == 3:
    print("돼지띠")
elif index == 4:
    print("쥐띠")
elif index == 5:
    print("소띠")
elif index == 6:
    print("호랑이띠")
elif index == 7:
    print("토끼띠")
elif index == 8:
    print("용띠")
elif index == 9:
    print("뱀띠")
elif index == 10:
    print("말띠")
elif index == 11:
    print("양띠")
elif index == 0:
    print("원숭이띠")

