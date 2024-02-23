# 174,175 번 파일을 실행시키면 현재 포켓몬이라는 폴더가 생성됬을 거에요
# 001_이상해씨.png 를 대상으로 pillow library 실습을 진행하겠습니다.


from PIL import Image

img = Image.open("포켓몬/001_이상해씨.png")
print(type(img)) # img 도 인스턴스였구나!!
print(dir(img)) # 뭐할 수 있는지보자
img.size  # 이미지의 사이즈를 반환합니다.
img.filename # 파일의 이름
img.format # 파일형식
img.mode # 색상모드
   # 이미지 보기
img.resize(  (100,100)   ) # x, y 의 튜플값이 들어간다.
                                          # 그리고, resize 자체만으로 img 가 변화되지 않는다.
img = img.resize((200,200))
img.show()
# img.save (    )         # 이미지 파일저장

# img.getpixel(  좌표의 튜플값  )
# img.putpixel( 좌표의 튜플값 ,  RGB(a)값 )

# ex1)
# img.getpixel((0,0))     0,0 의 색상반환
# img.putpixel((0,0), (255,255,255))      0,0 의 색상 변환

