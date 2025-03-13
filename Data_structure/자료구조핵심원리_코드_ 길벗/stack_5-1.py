class Stack:
    def __init__(self):
        self.container = list()  # 내부 표현 : 실제로 데이터를 담을 객체는 동적 배열
    
    def empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def push(self, data):
        self.container.append(data)  # 맨 마지막 요소가 top : 동적 배열의 맨 마지막에 요소를 추가하는 것은 스택의 top에 요소를 추가하는 것과 같음

    def pop(self):
        if self.empty():
            return None
        return self.container.pop()
    
    def peek(self):
        if self.empty():
            return None
        return self.container[-1]

s = Stack()
for i in range(1, 6):
    s.push(i)

while not s.empty():
    print(s.pop(), end = ' ')