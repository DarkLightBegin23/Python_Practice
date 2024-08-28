a = 1
def vartest(a):
    a = a + 2
    return a

a = vartest(a)
print(a)
a = vartest(a)
print(a)
