star = int(input())
r = star
for i in range(1, star + 1, 1):
    print(("*" * i).rjust(r))
    star += 1
