# 4880번 다음수
while True:  # 계속 세 수를 입력 받는데,
    a1, a2, a3 = map(int, input().split())
    if (a1, a2, a3) == (0, 0, 0):   # 모든 수가 0이면
        break  # 끝내기
    if a2 == ((a1 + a3) / 2):  # 등차수열
        print("AP", int(a3 + (a3 - a2)))
    elif a2 ** 2 == (a1 * a3):  # 등비수열
        print("GP", int(a3 * (a3 / a2)))