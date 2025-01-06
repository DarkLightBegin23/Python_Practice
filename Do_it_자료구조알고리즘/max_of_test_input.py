# 배열 원소의 최댓값을 구해서 출력(함수값 입력받음)

from max import max_of

print("배열의 최댓값을 구합니다.")
print("주의 : 'End'를 입력하면 종료됩니다.")

number = 0
x = []

try:
    while True:
        s = input(f'x[{number}]값을 입력하세요.:')
        if s == 'End':
            break
        x.append(int(s))  # 배열 맨 끝에 추가
        number += 1

    print(f'{number}개를 입력했습니다.')
    print(f'최댓값은 {max_of(x)}입니다.')
except IndexError:
    print("수를 입력하지 않았습니다.")
