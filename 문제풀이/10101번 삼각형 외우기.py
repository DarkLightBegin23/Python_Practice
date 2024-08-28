# 10101번 삼각형 외우기
A = []

for i in range(3):
    A.append(int(input()))

if A[0] == A[1] == A[2] == 60:
    print("Equilateral")
elif A[0] + A[1] + A[2] == 180:
    if A[0] == A[1] or A[1] == A[2] or A[2] == A[0]:
        print("Isosceles")
    elif A[0] != A[1] or A[1] != A[2] or A[0] != A[2]:
        print("Scalene")
else:
    print("Error")