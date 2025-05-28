result1 = [x * y for x in range(2, 10)
    for y in range(1, 10)]
print(result1)

a = [1, 2, 3, 4]
result2 = [num * 3 for num in a]
print(result2)

result3 = [num * 3 for num in a if num % 2 == 0]
print(result3)