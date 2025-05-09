# 2675번 문자열 반복
T = int(input())

for i in range(T):
    R, S = input().split()
    for x in S:
        print(x * int(R), end='')  # end='' 옆에 붙임(리스트 join하고 비슷한 듯)
    print()  # 줄바꿈
