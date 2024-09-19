# 300제 리스트부터
'''
# 300제 053
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054 del 메소드?
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]
print(movie_rank)

# 055
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 058 sum 메소드
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 060 평균
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)

# 061 리스트 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 066 join 메소드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 068
print("\n".join(interest))

# 069 문자열 split 메소드
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

# 070 정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
data2 = sorted(data)
print(data2)

# 072 튜플 == () 그리고 딕셔너리 == {}
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 073 튜플 정의(요소 뒤 콤마 꼭 붙이기)
my_tuple = (1, )
print(my_tuple)

'''
'''
튜플은 원소 값 변경 X
--> 새로 튜플을 정의해야 함

원칙적으로 괄호가 있어야 하나 없어도 동작
'''
'''
# 079 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 range 함수
data = tuple(range(2, 100, 2))
print( data )

# 082~083 바인딩(star expression)
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores
print(valid_score)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, b = scores
print(valid_score)

# 085~ 딕셔너리
ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
print(ice)

ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

print("메로나 가격: ", ice["메로나"])

ice["메로나"] = 1300  # 값 수정

del ice["메로나"]  # 삭제
print(ice)

# 091~096번
inventory = {"메로나": [300, 20], 
             "비비빅": [400, 3], 
             "죠스바": [250, 100]}

print(inventory['메로나'][0])  # 딕셔너리 인덱싱 300 [키][딕셔너리]

inventory["월드콘"] = [500, 8]  # 딕셔너리_이름[키][value] --> 추가
print(inventory)

print(inventory.keys())
ice = list(inventory)
print(ice)
print(inventory.values())

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))  # 중첩된 values 값은 계산안되는 듯... ex) [500, 8]

icecream.update(inventory)
print(icecream)

# 099 zip 메소드
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))  # 각각 키와 밸류 값이 됩니당 zip(keys, values)
print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
'''
# 분기문

time = input("현재시간: ")
if time[-2:] == "00":  # 문자열 응용
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가좋아하는계절은: ")

if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():  # 이렇게 하면 value 값만 따로 판별할 수 있음
    print("정답입니다.")
else:
    print("오답입니다.")

환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")
'''
currency == values
'''

num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:  # num1이 제일 큰 경우
    print(num1)
elif num2 >= num1 and num2 >= num3:  # num2가 제일 큰 경우
    print(num2)
else:  # 그 외(num3이 제일 큰 경우)
    print(num3)
