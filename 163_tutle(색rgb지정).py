import turtle as t
from time import sleep
 
t.shapesize(20) 
t.colormode(255)          # 이걸 꼭 지정해주어야함
for i in range(0,255,20):           
    for j in range(0,255,20):
        for k in range(0,255,20):
            t.color(j,i,k)                 # 그냥 rgb 값을 계속 변화하는 걸 지켜보기위함 ~

t.mainloop()