import random

a = random.randint(1, 6) # 1부터 6까지 랜덤으로 수 선택 후 a에 대입
print(a)

locate = ["대치", "여의도", "뚝섬", "위례", "천호", "잠실", "서현", "수원"] # locate 리스트 생성

b = random.choice(locate) # locate 리스트 중 랜덤으로 출력

print(b)