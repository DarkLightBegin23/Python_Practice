# 11720번 숫자의 합
su = int(input())
a = list(map(int, input()))
result = 0

if su > 0 and su <= 100:
    for i in range(su):
        result += a[i]
print(result)