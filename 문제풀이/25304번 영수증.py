# 25304번 영수증
X = int(input())  # 총 금액
N = int(input())  # 물건 종류 수

def calc(x, y):  # (함수 연습)
    z = x * y
    return z

a_list = list()  # 리스트 정의하는 두가지 방법
b_list = []
result = 0   # 총 금액과 비교할 변수

for i in range(N):  # 물건 품목 종류 수만큼 반복
    a, b = map(int, input().split())  # a == 품목 가격, b == 갯수
    a_list.append(a)
    b_list.append(b)

for i in range(N):  # 함수 써먹어서 result에 모조리 더하기
    cal1 = calc(a_list[i], b_list[i])
    result += cal1

if X == result:  # 조건문(둘이 일치하면 Yes, 다르면 No)
    print("Yes")
else:
    print("No")