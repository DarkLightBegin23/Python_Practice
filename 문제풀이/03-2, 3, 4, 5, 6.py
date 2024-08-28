# 03-2

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
    
print(result)    # 166833 출력

# 03-3
j = 0
while True:
    j += 1
    if j >= 6:break
    print("*" * j)
    
# 03-4
for i in range(1, 101, 1):
    print(i)
    

# 03-5
'''
score = [70, 60, 55, 75, 95, 90, 80, 85, 100]
for k in range(len(score)):
    k = sum(score)
    
average = k / len(score)
print(average)

'''

A = [70, 60, 55, 75, 95, 90, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total / len(A)
print(round(average, 1))


# 03-6

numbers = [1, 2, 3, 4, 5]
result = [2 * x for x in range(6) if x % 2 == 1]
print(result)