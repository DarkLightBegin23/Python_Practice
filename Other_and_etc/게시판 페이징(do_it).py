def get_total_page(m, n):
    if m % n == 0:
        return m // n  # m을 n으로 나눌 때 소수점 아래 자리를 버리기 위해 // 연산자 사용
    else:
        return m // n + 1

print(get_total_page(5, 10))  # 1 출력
print(get_total_page(15, 10))  # 2 출력
print(get_total_page(25, 10))  # 3 출력
print(get_total_page(30, 10))  # 3 출력

for i in range(1, 31):
    if i % 10 == 5 or i == 30:
        m = get_total_page(i, 10)
        print(m)
        
    