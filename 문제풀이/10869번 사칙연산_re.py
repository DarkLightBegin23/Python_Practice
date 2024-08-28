A, B = map(int, input().split())

cal = [A + B, A - B, A * B, A / B, A % B]

if (0 < A <= 10000) and (0 < B <= 10000):
    for i in cal:
        print(int(i))
    
else:
    pass
