# 네 번째 점
point_list1 = []

for a in range(3):  # 직사각형의 세 점 x, y 좌표를 입력받음.
    a = list(map(int, input().split()))
    point_list1.append(a)
    
answer = []
# XOR연산 x 좌표 - 세 개의 점 중 두 개의 점의 x 좌표가 동일하면, 
# 0이 되어 제거되고, 남은 하나가 네 번째 x 좌표가 되는 형태
answer.append(point_list1[0][0]^point_list1[1][0]^point_list1[2][0])
# XOR연산 y 좌표 - 세 개의 점 중 두 개의 점의 y 좌표가 동일하면,
# 0이 되어 제거되고, 남은 하나가 네 번째 y 좌표가 되는 형태
answer.append(point_list1[0][1]^point_list1[1][1]^point_list1[2][1]) 
# XOR연산은 중복된 값을 제거하는 것에 핵심이 맞춰져 있고, 
# 한꺼번에 연산이 진행돼서 세 개의 값 중 동일한 것을 제거하는 것에 초점이 맞춰져 있음!
print(answer)