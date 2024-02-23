import turtle as t

N = int(input("몇 각형을 그릴래요 ? "))

# 여기서 모든 다각형의 외각의 합은 360 도라는 것을 이용해봅시다.
# 3각형의 경우 120
# 4각형의 경우 90
# 5각형의 경우 72
# N 각형의 경우 360/N 이 되겠죠?
t.shape("turtle")
t.shapesize(3)
t.pensize(5)
t.color("red")

for i in range(N):            # 단순하게 N 각형은 변이 N 개니까!!! 
    t.forward(100)           # N번 반복하도록 설정!! 그리고 turn 그리고 turn 이 과정을 N번 하면됩니다.
    t.left(360/N)              

t.mainloop()