k = []

for i in range(11):
    k.append(i)
k_re = k[::-1]

for j in [k, k_re]:
    print(j)
    print(j * 2)

