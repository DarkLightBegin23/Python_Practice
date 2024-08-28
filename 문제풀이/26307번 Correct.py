# 26307번 Correct
HH, MM = map(int, input().split())

if 9 <= HH <= 11:
    print(60 * (HH - 9) + MM)  # 11시 59분 --> 179 == (60 * (11 - 9) + 59)

'''
결국 핵심은 저 식을 도출하는 데 있었구나...ㅜㅜ
'''