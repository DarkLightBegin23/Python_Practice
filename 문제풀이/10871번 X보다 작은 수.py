# 10871번 X보다 작은 수
N, X = map(int, input().split())  # N만큼 A 갯수를 일단 받을 거임, X는 기준이 되는 수
A = list(map(int, input().split()))  # A 리스트에 N만큼 숫자를 넣장

if N > 0 and X > 0 and N <= 10000 and X <= 10000:  # N과 X의 조건에 따라 범위 정함
    for i in range(N):  # N번 반복해서
        if A[i] < X:  # A 리스트의 요소 중에서 i번째 수가 X보다 작으면?
            print(A[i], end = ' ')  # 그 요소를 출력할거구 출력하고 한칸씩 띄어쓸거임.