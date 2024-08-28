# 5554번 심부름 가는 길

A = int(input())
B = int(input())
C = int(input())
D = int(input())

Y = A + B + C + D
X = Y // 60

Y = Y - (X * 60)

print(X)
print(Y)