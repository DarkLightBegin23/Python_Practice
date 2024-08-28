N = int(input())

if N > 0 and N < 10:
    for i in range(1, 10, 1):
        print(f"{N} * {i} =",N*i)