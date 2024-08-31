# 10156번 과자
K, N, M = map(int, input().split())

need = K * N - M  # 필요한 돈 계산

if need >= 0:  # 필요한 돈이 0보다 클 때만 need 값 출력
    print(need)
else:  # 가진 돈이 넘쳐나서 need 값이 음수 값이 나오면, 0 출력
    print(0)