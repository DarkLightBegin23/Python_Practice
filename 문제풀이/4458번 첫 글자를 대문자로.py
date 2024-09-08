# 4458번 첫 글자를 대문자로
N = int(input())

for i in range(N):  # N만큼 반복
    s = input()  # 문자열 받기
    m = s[0].capitalize()  # capitalize(), upper랑 같은 듯
    print(m+s[1:])