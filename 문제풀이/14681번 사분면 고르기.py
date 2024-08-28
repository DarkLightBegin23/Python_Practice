# 14681번 사분면 고르기
X = int(input())
Y = int(input())

if X == 0 or Y == 0:
    pass
else:
    if X > 0:
        if Y > 0:
            print(1)
        if Y < 0:
            print(4)
    if X < 0:
        if Y > 0:
            print(2)
        if Y < 0:
            print(3)