import turtle as t

# 거북이는 처음에 0,0 에 위치해있으며
# 0도(오른쪽)을 바라보고있습니다.

t.shape("turtle") # 커서 설정
t.shapesize(4) # 커서 크기 설정
t.pensize(7) # 선의 굵기 설정
t.color("red")  # 색 설정
t.getshapes()  # 커서로 설정할 수 있는 것들 반환
t.penup()  # 펜을 든다. (이동간 선을 그리지 않음)
t.pendown() # 펜을 내린다. (이동간 선을 그림)
t.forward(X) # X 만큼 앞으로 이동
t.left(N) # N 도 만큼 왼쪽으로 돈다
t.right(N) # N 도 만큼 오른쪽으로 돈다
t.goto(x좌표, y좌표) # x,y 로 이동
t.hideturtle() # 커서를 숨김
t.showturtle() # 커서를 나타냄
t.speed(0) # 0 부터 1 까지 설정가능하며, 스피드를 나타냄 (0에 가까울수록 빠름)
t.write(text, font=(글씨체, 크기, 속성)) # 속성에는 bold italic 같은 값들이 들어감
t.mainloop()