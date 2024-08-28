# 31403번 A+B-C
A = int(input())
B = int(input())
C = int(input())

Solve1 = A + B - C
strA_B = str(A) + str(B)
Solve2 = int(strA_B) - C

print(Solve1)
print(Solve2)