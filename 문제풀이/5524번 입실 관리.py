# 5524번 입실 관리

N = int(input())

if (N <= 10):
    for i in range(N):
        name = input()
        if len(name) <= 20 and len(name) > 0:
            if (name.isupper):
                lower_name = name.lower()
            print(lower_name)
        else:
            break