# 10768번 특별한 날

M = int(input())
D = int(input())

if 0 < M < 2:
    print("Before")

if M == 2:
    if D < 18:
        print("Before")
    if D == 18:
        print("Special")
    if D > 18:
        print("After")
if 2 < M < 13:
    print("After")
else:
    pass