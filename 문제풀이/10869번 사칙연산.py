A, B = map(int, input().split())

if A > 0 and B > 0 and A <= 10000 and B <= 10000:
    print(int(A + B))
    print(int(A - B))
    print(int(A * B))
    print(int(A / B))
    print(int(A % B))
    
else:
    pass
