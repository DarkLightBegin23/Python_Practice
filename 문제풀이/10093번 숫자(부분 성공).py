# 10093번 숫자
num1, num2 = map(int, input().split())  # 두 수
num_list = []

A = min(num1, num2)  # 두 수 크기에 따라 작은 순서대로 정렬 대입
B = max(num1, num2)

if 0 < A < 1001 and 0 < B < 1001:  # 서브태스크
    for i in range(A+1, B):  # 사이의 수만큼 입력
        num_list.append(i)

if abs(A - B) <= 1:  # 두 수 사이에 숫자가 하나도 없는 경우
    n = 0
else:
    n = len(num_list)

print(n)  # 출력
for i in num_list:
    print(i, end=" ")
