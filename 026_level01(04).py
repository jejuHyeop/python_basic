# 수를 입력받고 절대값을 출력하는 프로그램

# 절대값이라는 수학적 개념을 코드로 옮겨보도록 하겠습니다!!
# 음수라면 -1 을 곱해주면되겠네요!

A = int(input("수 입력 :"))

if A < 0:
    print("절대값은",-A)
else:
    print("절대값은",A)

# 검색을 통해서 절대값 표현을 검색해보신분은 if 문자체를 사용하지 않아도 되셨을 거에요!
print(abs(A))
# 만약 함수로 구현되어있는 표현을 발견하면 사용하시면되요!!
# 오히려 좋은 습관입니다!!