# 9086번 문자열

T = int(input())
for i in range(T):  # T만큼 반복
    word = str(input()) # 문자열 T번만큼 입력
    print(word[0] + word[-1]) # 각각 앞글자와 뒷글자 출력
