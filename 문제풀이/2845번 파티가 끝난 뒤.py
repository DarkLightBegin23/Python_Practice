# 2845번 파티가 끝난 뒤
L, P = map(int, input().split())
People = list(map(int, input().split()))

LP = L * P

for i in People:
    print(i - LP, end=" ")