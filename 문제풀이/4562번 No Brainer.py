# 4562번 좀비 싫어요

N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    if a > b:
        print('NO BRAINS')
    else:
        print("MMM BRAINS")