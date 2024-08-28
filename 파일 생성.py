print("Life", "is", "too long")

f = open("화이팅.txt", 'w')
for i in range(1, 11):
    data = "%d 나는 꼭 행복해질거야\n" % i
    f.write(data)
f.close()