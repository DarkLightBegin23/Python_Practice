def add(a, b):
    return a + b

def mul(c, d):
    return c * d
a = int(input("a = "))
b = int(input("b = "))

c, d = map(int, input("c, d =").split())

print("%d, %d의 더한 값은 %d입니다." % (a, b, add(a, b)))
print(f"{c}, {d}의 곱한 값은 {mul(c, d)}입니다.")