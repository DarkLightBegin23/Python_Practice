# many_error.py
try:
    a = [1, 2]
    print(a[3])
    4 / 0 # 인덱싱 오류가 먼저 발생했으므로 4 / 0에 따른 ZeroDivisionError 오류는 발생하지 않음
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")