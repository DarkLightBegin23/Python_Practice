# 10817번 세 수
A, B, C = list(map(int, input().split()))  # map함수로 세 수 받기
num_list = list()  # 세 수 넣을 리스트

num_list.append(A)  # (이거 반복문으로 넣을 수 있을 것 같은데...)
num_list.append(B)
num_list.append(C)

N_list = sorted(num_list)  # 정렬...해서

print(N_list[1])  # 가운데 수 출력