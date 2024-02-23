# dictionary 는 자료끼리의 연관을 지어줄때 적합한 자료형입니다.
# key 와 value 의 구조로 이루어지며,
# 아래와 같이 초기화 합니다.

D = {}  # 이 때, set 와 헷갈리실텐데 set 의 초기화는 set() 입니다.

D = {1:"one", 2:"two",'3':"Three"}
# 자 1,2,'3' 은 각각 key 에 해당되고, "one","two","Three" 는 Value 에 해당됩니다.
# Dictionary 는 set 와 마찬가지로 순서없는 자료형입니다~
print(D[1])  # 여기서 1 은 key 값을 넣어준 것으로 index 가 아니라는 것을 잊지마세요
#print(D[3]) # 이게 에러가 나는 이유는 '3' 은 문자열이기 때문에
print(D['3']) # 이렇게 해줘야합니다.

# Dictionary 요소 추가
D[4] = 'four'
D['5'] = "five"    
print(D)     # 다음과 같이 요소를 추가해주면 됩니다.
# 기존의 있던 키값을 설정해줄경우에 갱신이 되는 것을 볼 수 있습니다.
D[4] = 4
print(D)

for i in D:
    print(i)           # for 문을 돌리게되면 key 값들만 나오는 것을 알 수 있어요

for i in D:
    print(f"key 값 {i} value 값 {D[i]}")

E = {1:"one",2:"two"}

# 참고로 E.keys()  >  key 들을 반환
#             E.values()  > value 들을 반환   알아만두세요~
print(sum(E)) #????????????????? key 값들을 합쳐줍니다.
                         # 하지만, 하나라도 숫자가 아니면 에러가남!! 거의안씀..


