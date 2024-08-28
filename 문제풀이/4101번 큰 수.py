# 4101번 앞 수가 더 클까용?
while True:  # 무한 입력 반복, 그러나 아래 if문 조건(A == 0 and B == 0)에 해당되면 프로그램 STOP(break)!!
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    if A > B:  # 문제 조건 : 앞 수가 더 클 때(A가 B보다 클 때) Yes!
        print("Yes")
    else:  # 나머지 경우 : 뒷 수가 더 클 때(A가 B보다 작을 때) No!
        print("No")