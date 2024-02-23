# for, if 가 병합된 문제를 해결해보도록 하겠습니다.
# 1~99의 짝수를 모두 출력하는 프로그램을 작성하세요.

# 1 에서 99 까지 반복시키고, 짝수를 if 로 검증하면 되겠구나!!
for i in range(1,100):  # 1에서 99까지 반복시키고!
    if i % 2 == 0:      # 짝수를 판별하면 되겠구나
        print(i)

# i 라는 녀석을 너무 복잡하게 생각하지 마시고
# 알아서 1 에서 99 까지 돌아가는 녀석으로 보시는게좋아요

# range 를 적절하게 활용해서 if 사용하지 않기
for i in range(2,100,2):
    print(i)

# 위 아래 같은 결과지만, 아래의 방법은 반복횟수가 절반으로 줄어듭니다!!!
# 이말을 꼭 이해해보세요. (hint : i 값을 확인해보세요)
