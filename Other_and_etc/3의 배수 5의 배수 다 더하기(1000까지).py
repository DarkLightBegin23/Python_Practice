i = 0
n = 0

for i in range(1, 1000):  # while i < 1000:
    i = i + 1
    if i % 3 == 0:
        n += i
    if i % 5 == 0:
        n += i
print(n)