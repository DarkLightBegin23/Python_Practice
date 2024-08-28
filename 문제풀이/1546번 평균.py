# 1546번 평균
n = int(input())   # 과목 수
score = list(map(int, input().split()))  # 받은 점수 리스트

MaxScore = max(score)  # 점수 계산을 위한 리스트 및 score 최댓값과 새 변수 생성
New_list = list()
New_aver = 0 

for i in range(n):   # 과목 수만큼 반복
    New_score = (score[i] / MaxScore) * 100  # 새로운 점수 계산법
    New_list.append(New_score)  # 새 점수를 점수 리스트 넣음
    New_aver += New_list[i] / n  # 평균값을 각각 계산해서 더함

print(New_aver)