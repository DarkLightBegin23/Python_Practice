# 2742번 기찍 N
A = int(input())
B = []
for i in range(A):
    B.append(i)

B_reverse = sorted(B, reverse = True)

for i in B_reverse:
    print(i+1)