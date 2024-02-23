# 읽는 권한은 r 입니다.
# f.read() > 파일전체를 읽어옴
# f.readline() > 한줄을 읽음
# f.readlines() > 라인들단위로 리스트로 끊어줌
f = open("test_03.txt","r")
print(f.read())
f.close()

f = open("test_03.txt","r")
print(f.readline())
f.close()

f = open("test_03.txt","r")
print(f.readlines())
f.close()