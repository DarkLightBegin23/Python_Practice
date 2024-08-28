# 10430번 나머지 구하기

A, B, C = map(int, input().split())

if (A and B and C) > 1 and (A and B and C) <= 10000:
    Ans1 = (A + B) % C
    Ans2 = ((A % C) + (B % C)) % C
    Ans3 = (A * B) % C
    Ans4 = ((A % C) * (B % C)) % C
    
for i in [Ans1, Ans2, Ans3, Ans4]:
    print(i)