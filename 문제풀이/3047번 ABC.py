# 3047번 ABC
num_list = list(map(int, input().split()))  # 필요한 리스트들과 문자열
abc = input()
ABC_num = list()

ABC = list(abc)  # 문자열 각각의 문자를 리스트로
num_list.sort()  # 리스트 숫자 순서대로 정렬

for i in range(len(ABC)):  # 3번 반복
    if ABC[i] == 'A':  # A일 때
        ABC_num.append(num_list[0])  # 1번째 수 대응
    elif ABC[i] == 'B':  # B일 때
        ABC_num.append(num_list[1])  # 2번째 수 대응
    elif ABC[i] == 'C':  # C일 때
        ABC_num.append(num_list[2])  # 3번째 수 대응

print_num = " ".join(map(str, ABC_num)) 
'''
빈칸 만들어서 문자열로 만들기 (map으로 숫자 담고 있는 리스트 값들을 문자열로 변환 후 join을 이용해서 문자열 출력)
'''
print(print_num)  # 출력