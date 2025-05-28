def add_and_mul(a, b):
    return a + b, a * b  # return (a + b, a * b)

result = add_and_mul(3, 4)

# 여기서 return은 (7, 10)인 하나의 튜플 형태의 객체로 반환함
print(result)

# 확인용
print(type(result))  # 출력: <class 'tuple'>
print(result[0])     # 출력: 7
print(result[1])     # 출력: 10