# 27866번 문자와 문자열
S = str(input())
i = int(input())

if i <= abs(len(S)) and i > 0:
    print(S[i-1])