# 단별로 구구단 출력 ( 가로 )
# 어디가 많이 바뀐다?
# A x B
# A죠!!

for i in range(1,10):
    for j in range(2, 10):
        print(j, "X", i, "=", j*i, end="\t")

# 아마 기획부터 하신분은 금방 이해하실거에요
# 여기다 end 속성 복습까지!! 꼭 알아두세요         