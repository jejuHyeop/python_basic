import turtle as t
import random as r  # 색깔rbg 바꿔주기위해

# 함수1. 상하좌우 이동 : 각도조정과 이동하는 코드를 묶으면 되겠죠?
def 위로이동():
    t.setheading(90)
    t.forward(100)
def 아래로이동():
    t.setheading(270)
    t.forward(100)
def 우로이동():
    t.setheading(0)
    t.forward(100)
def 좌로이동():
    t.setheading(180)
    t.forward(100)



t.pensize(10)
t.shape("turtle")
t.colormode(255) # color 를 rgb 를 통해서 설정해줄수있음
t.color(0,0,0)    # rgb 가 0,0,0 이면 검은색입니다~~ 
t.speed(0)

t.listen()   # 이벤트처리를 위해 사용자의 이벤트를 듣고있겠다~
# t.onkey(F, key)  key를 누르면 F 함수를 실행하겠다~~
# t.onkeypress(F, key) key를 누르고 있으면 F 함수를 실행하겠다~  
# 여기서 key 로 넣을 수 있는 값들이 정해져있습니다!!
# 대소문자를 꼭 구분해서 넣어주셔야해요
t.onkeypress(위로이동, "Up")
t.onkeypress(아래로이동, "Down")
t.onkeypress(좌로이동, "Left")
t.onkeypress(우로이동, "Right")

# 함수2. 원점이동 ( home 이라는 함수도 있긴하대요! )
def 원점이동():
    t.penup() # 기본적으로 pendown 이 되어있어요!! 그래서 goto 를 하면 선이 생기겟죠?
    t.goto(0,0) 
    t.pendown() 

t.onkeypress(원점이동, "space")


# 함수3. 색깔바꾸기    
def 색바꾸기():
    t.color(r.randint(0,255),r.randint(0,255),r.randint(0,255))

t.onkeypress(색바꾸기, "c")


# 함수4. 펜두께 바꾸기 (10,20,30,40,50,60,70,80 순환)
두께 = 1
def 두께바꾸기():
    global 두께                  # 이게 핵심이에요!! 저희 함수배울때
    두께 += 1                    # 입력값만으로 구현을 해야된다고 했는데
    t.pensize((두께%8+1)*10) # 현재 입력값이 없는데 두께라는 값을 이용하고 있죠
                                                 # 즉, 저기에있는 두께라는 변수는 
                                                # 함수내의 값이 아니라
                                                # 53 번째 줄에 있는 변수를 가져와서 사용하겠다는 거에요
                                                # 변수에는 지역변수와, 전역변수가 존재합니다.
                                                # 이부분은 여러분과 코딩을 할때, 따로 다루진 않았는데
                                                # 아시면 분명히 도움이 됩니다.
                                                # 쉽게말해서, 변수를 어디서 사용할 수 있는지에 대해서 기준을 나눈거에요

                                                # 전역변수 : 코드 전체에서 사용할 수 있는 변수
                                                # 지역변수 : 특정 지역에서만 사용할 수 있는 변수

                                                # 쉽게 구분하는 방법은 함수안에서 사용된 변수는 지역변수입니다.
                                                # 예를들어
                                                # def add(x,y):
                                                #      z = x+y
                                                #      return z
                                                # 자, 여기서 x,y,z 모두를 지역변수라고 해요.
                                                # 함수를 빠져나가는 순간 x,y,z 는 사용할 수 없어요
                                                # 나머지의 경우는 다 전역변수에 속한다고 생각하시면되요.

                                                # 하지만 "두께바꾸기" 와 같이 전역변수를 필요로 하는 코드에서는 
                                                # ( 두께라는 것이 함수가 동작할 때마다 바껴야함으로!! )
                                                # global 이라는 것을 명시해줌으로써
                                                # 전역변수로 선언되어있는 두께를 지정해줄 수 있어요
                                                # 지역변수와 전역변수는 따로 파일을 만들어서 다뤄볼게요
                                                
t.onkeypress(두께바꾸기, "d")

# 함수5. 펜 up, down 상태변화 함수
pen = True
def 펜상태변화():
    global pen
    if pen:
        pen = False
        t.penup()
    else:
        pen = True
        t.pendown()

t.onkeypress(펜상태변화, "p")

t.mainloop()



    