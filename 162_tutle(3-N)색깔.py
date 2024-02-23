import turtle as t

N = int(input("몇 각형을 그릴래요 ? "))

t.shape("turtle")
t.shapesize(3)
t.pensize(5)
t.color("red")
t.speed(0)        

색 = ["red", "green", "yellow", "blue", "brown", "gray"]  

for i in range(3,N+1):             
    # i 가 바뀔때마다 즉, i 각형을 그린다고 표현했을 때 그리는 각형이 바뀔때마다
    # 색을 바꿔주면 되겠죠?
    # t.color(색[i]) 이렇게 되면 i 가 list 의 크기를 넘어가는 경우가 생깁니다.
    # 따라서 인덱스를 0 ~ list 의 크기 -1  로 설정해주어야 합니다.
    # 아~~~~~~~~~~~~~~~무리 큰수도 % N 를 사용하면 어떻게 된다고요?
    # N 개의 값들이 나온다는 것이죠!
    t.color(색[i%len(색)])
    for j in range(i):            
        t.forward(100)          
        t.left(360/i)  
t.mainloop()

