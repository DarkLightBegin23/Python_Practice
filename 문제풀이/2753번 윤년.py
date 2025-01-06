# 2753번 윤년
Year = int(input())

if Year > 0 and Year <= 4000:
    if (Year % 4 == 0) and (Year % 100 != 0) or (Year % 400 == 0):  # 윤년은 연도가 4의 배수이면서(and), 100의 배수가 아닐 때 또는(or) 400의 배수일 때이다.
        print(1)
    else:
        print(0)