# 2506번 점수 계산
N = int(input())
Solve = list(map(int, input().split()))
Score = 0
Plus = 0

for i in range(N):
    if Solve[i] == 1:
        Plus += 1
        Score += Plus
    else:
        Plus = 0

print(Score)