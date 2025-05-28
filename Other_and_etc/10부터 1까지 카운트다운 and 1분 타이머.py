# 10부터 1까지 카운트다운 and 1분 타이머

i = 10
while i > 0:
    print(i)
    i -= 1
print('땡!')

import time

i = 60
while i > 0:
    print(i)
    i -= 1
    time.sleep(1)
print('땡!')
