# 5597번 과제 안내신 분
Student = [int(input()) for x in range(28) if x <= 30]  # 1~30까지 숫자를 2개 제외하고 받음

for i in range(1, 31):  # 1~30까지 반복을 하는데 (30까지니까 31(n-1))
    if i not in Student:  # 만약 i에 Student 리스트 안에 없는 숫자가 나오면,
        print(i)  # 그걸 출력하는거야

'''
핵심은 not in 인듯...
'''