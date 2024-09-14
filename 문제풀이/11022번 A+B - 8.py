# 11022번 A+B - 8
T = int(input())

for i in range(1, T+1):  # T번 반복
    A, B = map(int, input().split())
    print(f'#Case #{i}: {A} + {B} = {A+B}')  # 형식대로 출력