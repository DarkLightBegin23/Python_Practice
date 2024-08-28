n = int(input())            # n개만큼 수를 입력할 거임. 알겠징?
arr = list(map(int, input().split()))       # arr 리스트에 띄어쓰기 기준으로 n개만큼 숫자를 담아.
v = int(input())            # 거기서 v에다가 해당하는 수 중에 개수를 구하고자 하는 수를 넣어담아.

count = 0           # 그걸 세서 넣으려는 변수임.

for i in range(n):         # for 반복문을 n번까지 돌려.
    if arr[i] == v:         # if 조건문으로 arr 리스트에서 v에 해당하는 수를 인덱싱해가지고
        count += 1          # 인덱싱해서 나오는 만큼 카운트 변수에 1를 더하면 돼

print(count)           # 이제 출력하면 끝이양.
