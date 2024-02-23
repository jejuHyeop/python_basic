# score.txt 를 읽고, 평균이 추가된 파일 "avg.txt" 로 저장해라

f = open("score.txt","r",encoding="utf-8")
f.readline()   # 이 줄의 의미를 잘생각하셔야해요!! 파일포인터가 첫줄을 지나게 해주는 구문!!

점수들 = f.readlines()
#print(점수들)       # 이렇게 확인하는 작업을 계속적으로 해주셔야해요!!

h = open("avg.txt","w",encoding="utf-8")
h.write("국어\t수학\t과학\t평균\n")

for i in 점수들:
    # i                                            "국어점수\t수학점수\t과학점수\n" 로 잘립니다!
    # i.replace("\n","")                "국어점수\t수학점수\t과학점수" 자르기 딱좋죠?
    # i.replace("\n","").split("\t")    [ 국어점수, 수학점수, 과학점수 ] 로 잘립니다.
    점수 =  i.replace("\n","").split("\t") 
    kor = int(점수[0])
    mat = int(점수[1])
    sci = int(점수[2])
    avg = (kor + mat + sci)/3
    h.write(f"{kor}\t{mat}\t{sci}\t{avg}\n")

f.close()
h.close()

