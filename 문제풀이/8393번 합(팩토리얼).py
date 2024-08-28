n = int(input())
sum = 0
if n <= 10000 and n >= 1:
    for i in range(0, n, 1):
        i += 1
        sum += i
    print(sum)