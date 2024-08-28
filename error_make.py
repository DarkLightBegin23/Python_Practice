# error_make.py

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '호우':
        raise MyError()
    print(nick)
    
try:
    say_nick('천사')
    say_nick('호우')
except MyError:
    print('허용되지 않는 별명입니다.')
    
say_nick('천사')
say_nick('호우')
