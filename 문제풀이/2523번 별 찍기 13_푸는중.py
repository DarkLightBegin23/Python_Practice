# 2523번 별 찍기 13
K = int(input())  # 입력받기

for i in range(1, K+1):  # 갯수 늘리기
    print("*"* i)
for j in range(K-1, 0, -1):  # 역순
    print('*'* j)