# class 에서 함수를 사용할 때는 self 가 필수적입니다.
class 모험가:
    inte = 0
    strong = 0
    dex = 0
    luck = 0
    얼굴형태 = "남자얼굴1"
    def 걷는다(self):
        print(self)
        print("Walking")
    def 뛴다():
        print("running")
# 결론부터 말씀드리면, 해당 class 의 많은 인스턴스들이 함수를 접근할 때,
# 각각의 객체들을 구분해주기 위한 정보가 필요하기 때문입니다.

모험가1 = 모험가()
모험가2 = 모험가()
모험가3 = 모험가()
모험가4 = 모험가()
#....
모험가100 = 모험가()


print(모험가1)   # 모험가1이 위치한 주소값이 나오는데, 모험가 1 이 걷는다 함수를 실행하게될때 출력되는
                          # self 값을 확인해보세요!! 9 번째 줄!!!
모험가1.걷는다()  # self 값이 출력됩니다.

# 즉, 함수의 self 는 각각의 객체들의 주소가 들어가있습니다.

