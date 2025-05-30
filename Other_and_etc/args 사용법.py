# 함수 add_mul은 choice에 따라 덧셈 또는 곱셈을 수행합니다.
# *args는 가변 인자를 의미
# 전달받은 여러 개의 값을 하나의 튜플로 처리합니다.

def add_mul(choice, *args):
   
    # choice가 "add"이면 덧셈 수행
    if choice == "add":
        result = 0  # 초기값은 덧셈이므로 0
        for i in args:  # args는 (1, 2, 3, 4, 5)와 같은 튜플 형태
            result = result + i  # 각 요소를 순차적으로 더함
   
    # choice가 "mul"이면 곱셈 수행
    elif choice == "mul":
        result = 1  # 초기값은 곱셈이므로 1
        for i in args:  # args는 (1, 2, 3, 4, 5)
            result = result * i  # 각 요소를 순차적으로 곱함
   
    return result  # 최종 결과 반환

# 'add'를 선택하고 1~5까지의 숫자를 인자로 전달 (1 + 2 + 3 + 4 + 5)
result = add_mul('add', 1, 2, 3, 4, 5)
print(result)  # 출력: 15

# 'mul'을 선택하고 1~5까지의 숫자를 인자로 전달 (1 * 2 * 3 * 4 * 5)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)  # 출력: 120
