import os

def 폴더생성(폴더이름):
    if os.path.isdir(폴더이름):
        print(f"{폴더이름} 이미 존재합니다.")
    else:
        os.mkdir(폴더이름)