marks = [90, 57, 68, 46, 87]
for number in range(len(marks)):  # 리스트 요소 5, 그러므로 range(5) (0부터 4까지)
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))
