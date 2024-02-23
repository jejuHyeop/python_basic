# 파일 입출력 중
# 파일 open 
# 
# open(파일이름, 권한) : 파일포인터 반환 
# 권한 : 쓰기 권한(w), 읽기 권한(r), 덧붙여서 쓰기 권한(a)
# 권한은 한가지만 선택!
# f.write(문자열)  : 문자열을 파일에 입력
# f.close()        : 파일포인터를 제거
# 파일포인터를 꼭 제거해주는 습관을 들입니다!!
f = open("test_01.txt","w")
f.write("today_is_last_day")
f.close()

# 만약 w 권한이고, 파일이름을 동일하게 해줄경우
# 기존의 내용이 다 없어집니다.
f = open("test_02.txt","w")
f.write("today_is_last_day")
f = open("test_02.txt","w")
f.write("today_is_last_day")
f = open("test_02.txt","w")
f.write("today_is_last_day")
f.close()
# 이럴땐
f = open("test_03.txt","a")
f.write("today_is_last_day\n")
f = open("test_03.txt","a")
f.write("today_is_last_day\n")
f = open("test_03.txt","a")
f.write("today_is_last_day\n")
f.close()

# 한국어를 파일에 입력하거나 읽어오고 싶다면
# 권한 다음에 encoding='utf-8' 설정을 해주면 됩니다.