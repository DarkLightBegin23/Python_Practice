# 2476번 주사위 게임

n = int(input())

dice = []

for i in range(n):
    a, b, c = map(int, input().split())
    
    if a == b and b == c:
        dice.append(10000 + a * 1000)
    elif a == b or a == c or b == c:
        if a == c or a == b:
            dice.append(1000 + a * 100)
        elif b == c:
            dice.append(1000 + b * 100)
        else:
            dice.append(1000 + c * 100)
    else:
        dice.append(max(a, b, c) * 100)
    
print(max(dice))