H, M = map(int, input().split())

C = int(input())
H += C // 60  # 60으로 나눈 몫 - ex) 132 // 60 = 2 
M += C % 60  # 60으로 나눈 나머지 - ex) 132 % 60 = 12

if C >= 0 and C <= 1000:
    if M >= 60:
        H += 1
        M -= 60
    if H >= 24:
        H -= 24
print(H, M)