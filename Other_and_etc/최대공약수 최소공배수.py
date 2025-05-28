def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())

if n < 1001 and n > 0:
    for i in range(n):
        n1, n2 = map(int, input().split())
        if n1 <= 45000 and n1 > 0 and n2 <= 45000 and n1 > 0:
            print(lcm(n1, n2))