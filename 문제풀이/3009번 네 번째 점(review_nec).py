# 빈 리스트 두 개를 생성하여 x좌표와 y좌표를 각각 저장할 준비
point_x = []
point_y = []

# 3개의 점의 좌표를 입력
for i in range(3):
    # 사용자로부터 두 개의 정수를 입력받아 x, y로 나눔.
    x, y = map(int, input().split())
    # 입력받은 x좌표를 point_x 리스트에 추가
    point_x.append(x)
    # 입력받은 y좌표를 point_y 리스트에 추가
    point_y.append(y)

# 네 번째 점의 좌표를 찾기 위해 반복문 사용
for i in range(3):
    # 현재 x좌표가 point_x 리스트에서 1번만 등장한다면 그 좌표를 x로 설정
    if point_x.count(point_x[i]) == 1:
        x = point_x[i]
    # 현재 y좌표가 point_y 리스트에서 1번만 등장한다면 그 좌표를 y로 설정
    if point_y.count(point_y[i]) == 1:
        y = point_y[i]

# 최종적으로 찾은 네 번째 점의 좌표 출력
print(x, y)
