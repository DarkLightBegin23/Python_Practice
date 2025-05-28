a = [1, 2, 3, 4]
print(a)
a.append(5)
print(a)

x = [100, 200, 300, 400]
y = []
# [100, 400]
print(y)
y.append(x[0])
y.append(x[3])
print(y)
