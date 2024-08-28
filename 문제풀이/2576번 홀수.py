# 2576번 홀수
odd = list()
odd_list = list()
odd_sum = 0
odd_min = 0

for i in range(1, 8):  # 1 ~ 7 정수 받아서 odd 리스트에 넣기
    i = int(input())
    odd.append(i)

for number in range(len(odd)):  # odd 리스트에서 odd_sum에 홀수만 더하고 odd_min에는 odd_list에서 가장 작은 값 넣기 
    if odd[number] % 2 == 1:
        odd_sum += odd[number]
        odd_list.append(odd[number])
        odd_min = min(odd_list)

if (odd_list == []):  # 근데 odd_list가 비어 있는(홀수가 하나도 없는) 경우에는
    print(-1)  # -1 출력
else:  # 그 외엔 odd_sum, odd_min 출력
    print(odd_sum)
    print(odd_min)