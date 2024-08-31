# 2751번 수 정렬하기 2
import sys  # 빠른 입출력을 받기 위해 sys 모듈 불러옴 (그냥 input()으로 받으면 큰 수라 엄청 느려진다더라...)

N = int(input())  # N만큼 수 입력받기
N_ls = list()  # 정렬할 때 담을 리스트 생성 ==> 그냥 = [] 넣어도 됨.

for i in range(N):  # N번 수를 입력받을겨(어차피 리스트 인덱스는 0부터 세기 때문에 N-1번까지 N번 입력받게 됨) # input() 역할을 하는 sys.stdin.readline())
    N_ls.append(int(sys.stdin.readline()))  # 입력받은 수를 N_ls에 집어넣을겨

N_ls.sort()  # 오름차순으로 요소 정렬을 시킴

for i in N_ls: 
    print(i)  # 차례대로 출력