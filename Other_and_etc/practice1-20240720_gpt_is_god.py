def cal(x, y):
    x = int(input("어떤 수 하나를 입력해주세요: "))
    y = int(input("다른 수를 입력해주세요: "))
    
    operations = [
        ("+", x + y),
        ("-", x - y),
        ("%", x % y),
        ("*", x * y),
        ("/", x / y),
        ("//", x // y),
    ]
    
    for op, result in operations:  # for문의 바인딩 형식(리스트나 튜플의 요소를 반복하면서 각 요소를 두 개 이상의 변수로 동시에 바인딩하는 방법)
        print(f"{x} {op} {y}의 값은 {result}입니다.")
        
a, b = 0, 0
cal(a, b)