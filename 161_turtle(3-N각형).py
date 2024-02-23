import turtle as t

N = int(input("몇 각형을 그릴래요 ? "))

t.shape("turtle")
t.shapesize(3)
t.pensize(5)
t.color("red")
t.speed(0)

# 자 136번 파일과 다른건~ 3 각부터 N 각까지 즉, 우리가 짰던 코드를 
# 반복하면 되겠네요.
# 하나의 대상으로 짠 코드는 다음과 같으니 이 과정들을 반복하면 되겠죠?
# for i in range(N):            
#     t.forward(100)          
#     t.left(360/N)              

for i in range(3,N+1):            # i 각형만 돌아가면서 그려주면 되죠!!
    for j in range(i):            
        t.forward(100)          
        t.left(360/i)  
t.mainloop()


