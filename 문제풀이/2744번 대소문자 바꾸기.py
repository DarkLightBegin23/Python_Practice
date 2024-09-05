# 2744번 대소문자 바꾸기
String = input()  # 받을 거
changeStrlist = list()  # 변환을 위한 리스트
changeStr = str()  # 문자열로 바꾸려구요.

for i in range(len(String)):  # 인덱싱 반복
    if String[i].isupper() == True:  # 대문자면?
        changeStrlist.append(String[i].lower())  # 소문자로
    if String[i].islower() == True:  # 소문자면?
        changeStrlist.append(String[i].upper())  # 대문자로

changeStr = "".join(changeStrlist)  # 리스트를 문자열로 변환 후 다 이어붙임

print(changeStr)  # 출력