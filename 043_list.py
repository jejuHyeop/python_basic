# 리스트에서 자료를 추가, 수정, 삭제 
# 하고싶을 때 사용하는 표현들입니다.
# 외우지 말고, 필요할 때마다 
# 검색해서 사용해도 좋습니다.

li = [1, 2, 'abc', 2.1, 1, True]

print(li[0], li[3])

print(len(li))        # 요소의 개수

li.append("Hello")   
print(li)             # 요소 추가(끝)

li.insert(0, False)
print(li)             # 요소 추가(위치지정)

print(li.pop())       # 요소 삭제(반환)
B = li.pop()          # 요소를 반환해서 B 에 대입
print(B)

print(li.count(1))    # 리스트 내 요소의 개수 반환

print(li.index(1))   # 요소의 인덱스를 반환

print(li.extend([1,2,3]))   # 리스트에 여러값(리스트) 추가

A = li.copy()  # 리스트 깊은 복사

li.sort()      # 리스트 복사

li.reverse()   # 리스트 뒤집기

li.clear()    # 요소 전부 삭제 , 초기화

# 이 외에도 다양한 기능들을 할 수 있는데 외우지 마시고
# 각각 한번 씩 사용만 해보세요~
