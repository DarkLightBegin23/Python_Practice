# f-function(왕초보를 위한 파이썬)

def f_function(a, b):
    try:
        if a and b:
            return (a * b) + (a / b)
        elif a:
            return '불능'
        else:
            return '부정'
    except:
        return '다시 부탁합니다'

x, y = map(int, input().split())

print(f_function(x, y))
