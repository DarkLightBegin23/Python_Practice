# 10039번 평균 점수
total = 0

for i in range(5):
    i = int(input())
    if i < 40:
        i = 40

    total += i

print(total // 5)