coffee = 10
while True:             # while 반복문이 참(True)일 동안만 진행
    money = int(input("돈을 넣어 주세요 : "))       # int(input) 사용자의 숫자 입력을 받아들이기 위한 부분이래요... (+ 추가로 파이썬은 #을 주석 및 예외 처리한다는 것.)
    if money == 200:         # 만약 돈이 200원 들어왔다면
        print("커피를 줍니다.")          # python과 C의 출력 함수 차이
        coffee = coffee - 1             # 커피 한 잔 줄어들게 하기
    elif money > 200:           # 만일 if 때와 달리 200원 이상 들어왔다면
        print("거스름돈 %d를 주고 커피를 줍니다." % (money - 200))          #거스름돈 계산 지급 및 커피 제공
        coffee = coffee - 1
    else:         # 앞서 나온  두 가지 경우 다 아니라면 (즉, 200원 이하의 돈이 들어왔다면)
        print("돈을 다시 돌려 주고 커피를 주지 않습니다.")   
        print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:          # 커피 다 팔아서 없대요~ 이럴 경우엔?
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break        # 프로그램 중지
