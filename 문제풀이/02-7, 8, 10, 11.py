# 02-7(다시 고민해보기)

a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

# 02-8(다시 고민해보기) - 튜플 실수함
a = (1, 2, 3)
a = a + (4,)
print(a)

# 02-10
b = {'A':90, 'B':80, 'C':70}
export = b.pop('B')
print(b)
print(export)

# 02-11
a = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6]
aSet = set(a)
b = list(aSet)
print(a)
print(b)