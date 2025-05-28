mix = "아아이아이아아아아아이이이아아아이아아아아이아아아아이아이이"

countA = 0
countE = 0
for i in mix:
    if i == "아":  # mix.index(i) (Nope) >> 저건 문자열에 i가 있나 찾는 거일세
        countA += 1
    elif i == "이":
        countE += 1
    else:
        pass

print("'아'는", countA, "개", "'이'는", countE, "개")