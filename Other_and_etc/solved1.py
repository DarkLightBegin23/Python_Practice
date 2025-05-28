a, b = map(int,input().split())
x = int(input())
solved = [('+', a + b), ('-', a - b), ('*', a * b), ('/', a / b)]

for i, j in solved:
    print(f'{a} {i} {b} = {j}')

for k in range(x):
    print('', x)