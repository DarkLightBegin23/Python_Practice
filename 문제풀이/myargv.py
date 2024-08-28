# myargv.py # 04-8

import sys

inputnumber = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

sum = 0
for number in inputnumber:
    sum += int(number)
print(sum)