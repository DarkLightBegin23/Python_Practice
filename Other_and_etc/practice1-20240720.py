def cal(x, y):
    x = int(input("어떤 수 하나를 입력해주세요:"))
    y = int(input("다른 수를 입력해주세요:"))
    print(f"{x}+{y}의 값은 {x + y}입니다.")
    print(f"{x}-{y}의 값은 {x - y}입니다.")
    print(f"{x}%{y}의 값은 {x % y}입니다.")
    print(f"{x}*{y}의 값은 {x * y}입니다.")
    print(f"{x}/{y}의 값은 {x / y}입니다.")
    print(f"{x}//{y}의 값은 {x // y}입니다.")

a, b = 0, 0
cal(a, b)