# 04-1
'''
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
number = int(input())

print(is_odd(number))
'''
# 04-2
'''
def avg_numbers(*args): # 입력 개수에 상관없이 사용하기 위해 *args 사용
    result = 0
    for i in args:
        result += i
    return  result / len(args)

print(avg_numbers(1, 2))     # 1.5
print(avg_numbers(1, 2, 3, 4, 5))  # 3.0
'''

# 04-5
'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
'''

#04-6

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a') # 내용 추가 'a' 사용
f.write(user_input)
f.write("\n") #입력한 내용을 줄 단위로 구분 > 줄 바꿈 문자 삽입
f.close()

# 04-7
'''
f = open('test2.txt', 'r')
body = f.read() # test.txt의 내용을 body 변수에 저장
f.close()
body = body.replace('java', 'python') # body 문자열에서 
f = open('test2.txt', 'w') # 쓰기 모드로 변경
f.write(body)
f.close()
'''


# 04-8
'''
# myargv.py

import sys

inputnumber = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

sum = 0
for number in inputnumber:
    sum += int(number)
print(sum)
'''