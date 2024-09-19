# 11557번 내가 먹으면 달달한 그거
T = int(input())
School = []
Drink = []

for i in range(T):
    N = int(input())
    for j in range(N):
        S, L = input().split()
        L = int(L)
        School.append(S)
        Drink.append(L)

    idx = Drink.index(max(Drink))
    print(School[idx])
