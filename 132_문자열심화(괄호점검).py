# 문자열을 입력 받고, 괄호가 잘 닫혀있는 문장인지 점검하세요. ( 소괄호만 사용 )
# 괄호라는 개념은 열어주는 괄호가 나오고 닫아주는 괄호가 나와야합니다.
# ()()()() 라든지 ((((())))) 과 같은 표현은 가능하나
# st.count('(') == st.count(')') 일 것입니다.
# 하지만, 위 조건이 맞더라도 (()))() 과 같은 표현은 할 수 없습니다. 
# 자!! 여기서 논리적으로 접근해보죠
# ( 왼쪽 괄호를 만나면 + 1
# ) 오른쪽 괄호를 만나면 -1 을 해줄때!!!
# 상태를 검사하는 변수를 N 이라고 하겠습니다.
# N 은 무슨 수를 써도 0 이상이여야합니다
# 만약 -1 가 된다는 것은 현재 여는 괄호가 없다는 것이되겠지요??

N = 0
st = input("문장을 입력하세요 : ")
for i in st:
    if i == '(':
        N += 1
    if i == ')':
        N -= 1
    if N < 0:
        break
if N == 0:
    print("옳은 문장입니다.")
else:
    print("틀린 문장입니다.")


