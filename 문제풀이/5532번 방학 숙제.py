L = int(input())  # 방학 일 수
A = int(input())  # 국어 총 풀어야 하는 페이지
B = int(input())  # 수학 총 풀어야 하는 페이지
C = int(input())  # 하루에 풀 수 있는 국어 페이지 수
D = int(input())  # 하루에 풀 수 있는 수학 페이지 수

Korean = A / C
Math = B / D
Total = 0
Date = 0

if Korean > Math:
    Total = int(L - Korean)
else:
    Total = int(L - Math)

if L >= Total:
    if Math > Korean:
        Date = L - Math
        print(int(Date))
    else:
        Date = L - Korean
        print(int(Date))
else:
    pass
