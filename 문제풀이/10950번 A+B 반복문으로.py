# 10950번 A+B 반복문으로
attempt = int(input())
for i in range(1, attempt + 1, 1):
    a1, a2 = map(int, input().split())
    if 0 < a1 < 10 and 0 < a2 < 10:
        print(a1 + a2)
