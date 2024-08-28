# 02-4

pin = "881220-1068234"
print(pin[7])

# 02-5

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 02-6

a = [1, 3, 5, 4, 2]
a.sort()
b = a[:] # b = a 는 주소까지 같아져서 리스트 안 요소들이 같이 변경됨!
a.reverse()
print(a)
print(b)