# 96쪽 스택 자료구조를 이용한 괄호 문제 해결 코드

a_count = []

def push(push_data):
    a_count.append(push_data)
    
def pop():
    a_count.remove(a_count[-1])
    
a = input()

for i in a:
    if i == "(":
        push(i)
    elif i == ")": 
        pop()
    
if len(a_count) == 0:
    print('OK')
else:
    print('error')