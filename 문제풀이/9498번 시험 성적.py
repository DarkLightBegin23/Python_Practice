# 9498번 시험 성적
score = int(input())
if score <= 100 and score >= 0:
    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score < 90:
        print("B")
    elif score >= 70 and score < 80:
        print("C")
    elif score >= 60 and score < 70:
        print("D")
    else:
        print("F")
