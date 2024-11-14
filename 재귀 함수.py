def addFun(n, total=0):
    if n > 10:  # n이 10을 초과하면 재귀를 종료합니다.
        print("1부터 10까지의 합:", total)
    else:
        total += n
        addFun(n + 1, total)  # n을 1 증가시키면서 재귀 호출

addFun(1)

def FAC(j, total=1, initial_j=None):
    if initial_j is None:
        initial_j = j  # 초기 호출 시 j의 값을 저장합니다

    if j < 1:
        print(f"{initial_j}! = {total}")
    else:
        total *= j
        FAC(j - 1, total, initial_j)

FAC(3)