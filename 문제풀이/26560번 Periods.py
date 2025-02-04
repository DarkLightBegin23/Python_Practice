# 26560번 Periods

n = int(input())

for i in range(n):
    sentence = input()
    if sentence[-1] != '.':
        re_sen = sentence.rstrip() + '.'
        print(re_sen)    
    else:
        print(sentence)
