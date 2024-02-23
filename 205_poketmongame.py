import random
import os
from tkinter import messagebox
from tkinter import *


tk = Tk()

tk.title("pokeMon")
tk.geometry("500x550")

score = 0
life = 5

포켓몬목록 = os.listdir("포켓몬그림자")
la_life = Label(tk, text="♥"*life + "♡"*(5-life),fg='red',font=("맑은고딕",30,"bold"))
la_life.pack()
la = Label(tk)
la.pack()


btn = [None] * 5
for i in range(5):
    btn[i] = Button(tk, width=20, font=("맑은고딕",15,"bold"), fg="navy", command=lambda k=i: 판단(k))
    btn[i].pack()


def 판단(N):
    global score, life
    if 보기인덱스[N] == 정답인덱스:
        img = PhotoImage(file=f"포켓몬250/{포켓몬목록[정답인덱스]}")
        la.image=img
        la.config(image=img)
        messagebox.showinfo("Correct!!", "U R Genius~")
        change() 
        score += 100      
    else:
        life -= 1
        la_life.config(text="♥"*life + "♡"*(5-life))
        if life == 0:
            messagebox.showwarning("Nope :( ",f"Your score : {score}")
            exit()


def change():
    global 정답인덱스, 보기인덱스
    정답인덱스 = random.randint(0, len(포켓몬목록)-1)
    img = PhotoImage(file=f"포켓몬그림자/{포켓몬목록[정답인덱스]}")
    la.config(image=img)
    la.image = img
    보기인덱스 = {정답인덱스}
    while True:
        보기인덱스.add(random.randint(0, len(포켓몬목록)-1))
        if len(보기인덱스) == 5:
            break
    보기인덱스 = list(보기인덱스)

    for i in range(5):
        이름 = 포켓몬목록[보기인덱스[i]].split("_")[1].split(".")[0]
        btn[i].config(text=이름)
change()
tk.mainloop()



# tk = Tk()

# tk.title("pokeMon")
# tk.geometry("600x600")

# l1 = Label(tk, text="뭘까요?", font=("맑은고딕", 26,"bold","italic"))
# l1.pack()


# tk.mainloop()