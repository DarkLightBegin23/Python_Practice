# 5596번 시험 점수
S = list(map(int, input().split()))
T = list(map(int, input().split()))

S_sum, T_sum = 0, 0

for i in range(4):
    S_sum += S[i]
    T_sum += T[i]


if S_sum > T_sum:
    print(S_sum)
elif S_sum == T_sum:
    print(S_sum)
else:
    print(T_sum)