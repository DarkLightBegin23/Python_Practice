# try_else문.py
try:
    age = int(input('나이를 입력하세요'))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 12:
        print("만 12세 이하입니다.")
    else:
        print("환영합니다.")