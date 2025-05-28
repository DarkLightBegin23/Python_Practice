score = [90, 55, 78, 43, 62, 49, 54, 70, 100, 94]       # 학생들의 시험 점수 리스트

number = 0          # 학생마다 붙여줄 번호
for marks in score:         # for문(반복문)
    number = number + 1
    if marks >= 60:
        print("%d번 학생은 합격입니다." % number)
    elif marks >= 50:
        print("%d번 학생은 재응시 대상입니다." % number)
    else:
        print("%d번 학생은 불합격으로 다음 기회에 다시 응시해주세요." % number)
