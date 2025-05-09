# 2738번 행렬 덧셈
# 두 개의 정수를 입력받습니다. 이는 행렬의 행 수와 열 수입니다.
a, b = map(int, input().split())

# 두 개의 빈 리스트를 만듭니다. x와 y는 각각 입력받을 행렬을 저장할 리스트입니다.
x, y = [], []

# 첫 번째 행렬을 입력받아 리스트 x에 저장합니다.
for row in range(a):
    row = list(map(int, input().split()))  # 한 행의 숫자들을 리스트로 변환합니다.
    x.append(row)  # 변환된 리스트를 x에 추가합니다.

# 두 번째 행렬을 입력받아 리스트 y에 저장합니다.
for row in range(a):
    row = list(map(int, input().split()))  # 한 행의 숫자들을 리스트로 변환합니다.
    y.append(row)  # 변환된 리스트를 y에 추가합니다.

# 두 행렬의 덧셈 결과를 출력합니다.
for row in range(a):
    for col in range(b):
        # 행렬 x와 y의 각 원소를 더하여 출력합니다.
        print(x[row][col] + y[row][col], end=' ')
    print()  # 한 행이 끝나면 줄을 바꿔서 다음 행의 결과를 출력합니다.
