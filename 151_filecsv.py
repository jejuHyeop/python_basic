# csv 파일은 , 쉼표를 기준으로 행을 구분합니다~

f = open("score.csv","r",encoding="utf-8")
f.readline()   # 이 줄의 의미를 잘생각하셔야해요!! 파일포인터가 첫줄을 지나게 해주는 구문!!

점수들 = f.readlines()
#print(점수들)       # 이렇게 확인하는 작업을 계속적으로 해주셔야해요!!

h = open("avg.csv","w",encoding="utf-8")
h.write("국어,수학,과학,평균\n")

for i in 점수들:
    점수 =  i.replace("\n","").split(",") 
    kor = int(점수[0])
    mat = int(점수[1])
    sci = int(점수[2])
    avg = (kor + mat + sci)/3
    h.write(f"{kor},{mat},{sci},{avg}\n")

f.close()
h.close()
