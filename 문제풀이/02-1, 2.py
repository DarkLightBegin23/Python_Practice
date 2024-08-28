#02 - 1
a = [80, 75, 67]
sum = 0
average = 0

for i in a:
    sum += i 
    average = sum / 3

print(int(average))

# 02-2
number = int(input("홀수 짝수 판별, 수를 입력해주세요 :"))

if number % 2 == 1:
    print("홀수")
else:
    print("짝수")