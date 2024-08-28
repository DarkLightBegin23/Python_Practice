H, M = map(int, input().split())

M -= 45
if M < 0:
    H -= 1    # ex) 2시 -1분 == 1시 59분 ((2-1)시 (-1+60)분)
    M += 60   # 상동
    if H < 0:   # ex) -1시 == 23시
        H = 23
print(H, M)
