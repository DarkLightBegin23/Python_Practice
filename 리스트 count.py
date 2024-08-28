my_list = list(map(int, input().split()))

var = my_list.count(3)

if var < 4 and var > 0:
    print("3의 개수가 4개 미만입니다.")
else:
    print(f"3의 개수가 {var}개입니다.")

my_b = [1, 2, 3, 4, 5, 6, 6, 7]

print(my_b[6])

my_b.pop(6)

print(my_b[6])
print(my_b.pop(0))
print(my_b)