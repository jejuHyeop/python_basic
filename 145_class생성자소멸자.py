# 생성자는 class 가 인스턴스를 생성할 때 자동으로 실행되는 함수를 말합니다.
# 소멸자는 인스턴스가 소멸할 때 자동으로 실행되는 함수를 말합니다.
# 생성자 함수의 기본형태는 def __init__(self):  입니다.
# 소멸자 함수의 기본형태는 def __del__(self):  입니다.

from time import sleep           # 소멸자를 더 잘 확인하기 위해 넣어줄겁니다!!
                                                # 그냥 실행하게 되면 생성자와 소멸자가 동시에 실행되는 것처럼 보일거거든요!

class 초보자:
    def __init__(self):
        print("캐릭터 생성")
    def 걷는다(self):
        print("걷는다.")
    def __del__(self):
        print("캐릭터 소멸")

A = 초보자()            # 생성하는 순간 생성자 함수가 실행!!
sleep(10)                # 10 초동안 코드실행을 멈춤
                                # 10 초 후에 코드가 종료되면서 소멸자 함수가 실행!!

# 예를들어 메이플스토리에서 캐릭터를 생성하게 되면, 
# 생성한 캐릭터에 대해서 처리해야하는 부분이 많을 것입니다.
# 개인 창고라던지, 서버에 닉네임 등록이라던지, 쪽지란 생성 같은 것들을 만들어줘야겠죠
# 반대로 캐릭터를 삭제할 때 해야하는 일들도 있어요
# 개인 창고공간을 소멸시키던지, 서버에 등록된 닉네임을 삭제한다던지 그런 것들을
# 생성자 소멸자에 명시해줍니다!!!