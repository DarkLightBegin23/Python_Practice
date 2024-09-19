# 300제 007
print("naver", "kakao", "sk", "samsung", sep=";")

# 300제 009
'''
print("first", "second", end=" ")
'''
print("first", end="");print("second")
'''
# 300제 013(012 +)
s = "hello"
t = "python"

print(s+"!", t)
print(type(s), type(t))
'''
# 300제 022
license_plate = "24가 2210"
print(license_plate[-4:])  # 거꾸로 인덱싱/슬라이싱함 : 0 == license_plate[-1]

# 300제 025~026
phone_number = "010-1111-2222"
number = phone_number.replace("-", " ")  # replace 메소드는 문자열의 단어 중 해당되는 것을 바꿔줌
print(number)

number2 = phone_number.replace("-", "")  # 공백 제거도 가능
print(number2)

# 300제 035 % 포맷팅
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s 나이 : %d" %(name1, age1))
print("이름 : %s 나이 : %d" %(name2, age2))

# 300제 036 format 메서드

print("이름 : {} 나이 : {}".format(name1, age1))
print("이름 : {} 나이 : {}".format(name2, age2))

# 300제 038
ss = "5,969,782,550"
ssd = ss.replace(",", "")
ssds = int(ssd)
print(ssds, type(ssds))

# 300제 040 strip()
data = "   삼성전자    "
data1 = data.strip()
print(data1)

# 300제 043 capitalize 메서드
a = "hello"
a = a.capitalize()
print(a)

# 300제 044~045 endswith 메소드
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))  # True

file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))

# 300제 046 startswith 메소드
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 300제 strip 메소드
ticker = "btc_krw"
print(ticker.split("_"))

# 300제 rstrip 메소드
data = "039490     "
print(data.rstrip())

