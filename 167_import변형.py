# 방법1. import A
import random       # random.py 를 가져옴

random.randint(1,2)
random.random()
random.gammavariate()  # 다음과 같이 random 이라는 표현을 계속 써줘야함...

# 방법2. from A import [Class or Function]
from random import randint, random, gammavariate

randint(1,2)
random()
gammavariate()   # 이 함수 외의 random 함수를 사용할 수 없음, 또 적어주면 되긴함

# 방법3. from A import *
from random import *

def randint():
    print("randint 못사용할걸??")

randint()
random()    # randint 라는 함수와 구별할 수 없으며, random 의 randint 가 실행되지 않음

# 방법4. import random as r
import random as r
r.randint(1,2)
r.betavariate()   # 저는 이방법을 택하겠습니다~~






