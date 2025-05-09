# 5086번 배수와 약수
while True: # while(1)
    x, y = map(int, input().split())
    if (x and y) == 0:
        break
    
    if y % x == 0:  # x가 y보다 크고 y가 x로 나눠서 나머지 0이면 약수
        print("factor")
    elif x % y == 0: # y가 x보다 크고 x가 y로 나눠서 나머지 0이면 약수
        print("multiple")
    else:
        print("neither")