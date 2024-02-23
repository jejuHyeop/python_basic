# set 형을 사용해서 로또번호를 생성해볼까요?
# N 을 입력받고, N회만큼 로또번호를 생성해봅시다!!
import random

N = int(input("로또 횟수입력 : "))

for i in range(1,N+1):     # 1 회 로또 번호는 같이 출력하기 위해 1~ N 까지의 반복으로 설정
    lotto = set()
    while True:              # lotto 번호를 생성할때 주의할것은 한회에 중복되는 수가 추가될 수 도 있기때문에
                                       # while True 로 설정!!
        lotto.add(random.randint(1,45))
        if len(lotto) == 6:
            break
    print(f"{i} 회 당첨번호 {lotto}")

