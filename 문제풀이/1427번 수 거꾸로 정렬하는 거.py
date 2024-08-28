su = int(input())

if su <= 1000000000 and su > 0:
    su = str(su)
    su_reverse = sorted(su, reverse = True)
    su_reverse = int(''.join(su_reverse))
    print(su_reverse)
else:
    pass