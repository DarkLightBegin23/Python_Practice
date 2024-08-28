# 4470번 줄번호
list_in = []  # 문자열 담을 리스트
num = int(input())  # num만큼 문자열 입력 받을 거임 ㅇㅇ
i = 0 # 얘로 앞에 단어 번호 매길거양

for a in range(num):  # num번 반복
    a = input()  # a에 문자열 입력
    list_in.append(a)  # list_in 리스트에 a 문자열을 num번 넣음

for j in list_in:  # 리스트 요소를 j에 대입하면서 다 출력할 때까지 반복
    i += 1  # 단어 번호 하나씩 증가시키자
    print(f'{i}.', j)  # f-string 이용해서 쉽게 '(단어 번호). (문자열)' 형태로 출력할거양