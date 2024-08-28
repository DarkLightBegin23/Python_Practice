A, B = map(int, input().split())
while (A and B) <= 10000 (A and B) >= -10000:
    if A < B:
        print("<")
        break
    elif A > B:
        print(">")
        break
    elif A == B:
        print("==")
        break