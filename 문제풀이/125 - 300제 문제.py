# 125 - 300제 문제
telephone_num = input("휴대전화 번호 입력 :")

telephone = ['SKT', 'KT', 'LGU+', '기타']

if telephone_num [2]== '1':
    print(f'당신은 {telephone[0]} 사용자입니다.')
elif telephone_num[2] == '6':
    print(f'당신은 {telephone[1]} 사용자입니다.')
elif telephone_num[2] == '9':
    print(f'당신은 {telephone[2]} 사용자입니다.')
elif telephone_num[2] == '0':
    print(f'당신은 {telephone[3]} 사용자입니다.')
else:
    print("없는 번호입니다.")