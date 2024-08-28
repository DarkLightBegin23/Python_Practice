# 2501번 약수 구하기
N, K = map(int, input().split())
P = []
for i in range(1, N+1):
    if N % i == 0:  # 몫이 i가 나와도 성립 (몫과 나누는 수 뒤집어도 상관 X)
        P.append(i)

if K > len(P):
    print(0)
else:
    print(P[K-1])
