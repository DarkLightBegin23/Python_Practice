# 10952번 A+B - 5
A = 0  # 입력할 수 선언
B = 0

while True:  # 계속 반복해서
    A, B = map(int, input().split())  # A, B 수를 연달아 받는데,
    if A == 0 and B == 0:  # 만약 A와 B가 다 0이 입력되었다면?
        break   # 프로그램 멈추기
    else:  # 그 외의 경우
        print(A + B)  # A+B 계산 출력
