x = int(input("첫번째 숫자를 입력해주세요 : "))
y = int(input("두번째 숫자를 입력해주세요 : "))

a = [("+", x + y), ("-", x - y), ("*", x * y), ("/", x / y), ("//", x // y), ("%", x % y)]

for i, result in a:
    print(f'{x} {i} {y} = {result}')

def yes():
    return print("아우내 화이팅")

yes()