try:  # try 블록에서 문제 없을 시 except 블록은 실행되지 않음..
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    print(a / b)
    print(c[5])
except (ZeroDivisionError, IndexError) as e: # 2개 이상의 오류를 동일하게 처리하기 위해서 괄호로 함께 묶어 처리
    print(e)
