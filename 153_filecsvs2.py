# 이번에는 1 ~ 20 까지의 csv 파일을 1개의 avg.csv 파일로 만들어볼까요??
# 이러면 끝이겠죠??? 4,5 번쨰랑 h.close() 만 신경써주세요~

h = open(f"avg.csv","w",encoding="utf-8")
h.write("국어,수학,과학,평균\n")

for i in range(1,21):
    f = open(f"score_{i}.csv","r",encoding="utf-8")
    f.readline()   # 이 줄의 의미를 잘생각하셔야해요!! 파일포인터가 첫줄을 지나게 해주는 구문!!

    점수들 = f.readlines()
    #print(점수들)       # 이렇게 확인하는 작업을 계속적으로 해주셔야해요!!

    for i in 점수들:
        점수 =  i.replace("\n","").split(",") 
        kor = int(점수[0])
        mat = int(점수[1])
        sci = int(점수[2])
        avg = (kor + mat + sci)/3
        h.write(f"{kor},{mat},{sci},{avg}\n")

    f.close()
h.close()
