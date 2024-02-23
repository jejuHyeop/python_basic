# 다음은 import 에 대해서 알아봅시다.
# import 를 위해 ex_01.py 과 ex_02.py 를 생성해주세요.
# import [  file   ]  을 통해서 file 안에 있는 클래스나 함수들을 해당 코드에서 사용할 수 있습니다.

# 자, 설명을 듣고 차례대로 해주셔야 이해하실거에요

# step1. ex_01.py 와 ex_02.py 를 각각 생성해서 다음과 같이 작성합니다.

class Maple:
    pass
print("test 용 입니다.")
# ex_01.py

import ex_01

A = ex_01.Maple
# ex_02.py

# step2. ex_02.py 에서 실행해보세요!!!
# 그럼 ex_01.py 에 있던 test용입니다가 보일겁니다!!
# 이말인 즉, import 를 하게될 때 ex_01 이 실행되는 것입니다.
# 근데 라이브러리같은 파일 즉, 다른 사람에게 import 가 많이되는 파일의 경우
# 저렇게 test 용입니다라는 문구를 출력하게 하면 안되요!!

# step3. 각각의 ex_01, ex_02 파일을 다음과 같이 수정해보세요.

class Maple:
    pass
print("여기는 ex_01",__name__)
print("test 용 입니다.")
# ex_01.py

import ex_01

A = ex_01.Maple
print("여기는 ex_02", __name__)
# ex_02.py

# step4. 다시 ex_02.py 에서 실행을 해봅니다.
# 그러면 여기는 ex_01 ex_01 이 나오고 여기는 ex_02 __main__ 이 나올겁니다.
# 이번에는 ex_01.py 에서 실행을 해봅니다.
# 여기는 ex_01 __main__ 이 나올겁니다.
# 이를 미루어 봤을 때, __name__ 이라는 녀석은
# 지금 해당파일이 누구에 의해 실행되는지에 대한 정보를 가지고 있습니다.
# 만약 자기자신이 실행파일일 경우 __main__ 을
# import 와 같이 자기자신이 실행하지 않았는데 실행되는 경우에는
# 해당 파일의 이름이 출력됩니다.

# step5. ex_01 를 다음과 같이 수정합니다.
class Maple:
    pass

if __name__ == "__main__":
    print("여기는 ex_01",__name__)
    print("test 용 입니다.")
# ex_01.py

# step6. ex_02 파일에서 실행해봅니다!!
# 그럼 53 번째 줄이 ex_02 파일에 의해 실행될테니!!!
# 아무것도 실행하지 않겠죠!!!
