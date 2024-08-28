n = int(input())

number = [int(input()) for n in range(n) if abs(n <= 1000)]

sorted = set(number)

srtnumber = list(sorted)  # srtnumber는 집합을 다시 리스트로 변환한 거
srtnumber.sort()

for n in range(len(srtnumber)):\
    
    print(srtnumber[n])