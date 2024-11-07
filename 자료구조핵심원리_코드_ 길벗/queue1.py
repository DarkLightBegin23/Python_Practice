class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False
        
    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        # 동적 배열의 맨 처음 데이터를 삭제하므로 빅오는 O(n)
        # 좀 더 효율적으로 구현할 수는 없낭...
        return self.container.pop(0)
    
    def peek(self):
        return self.container[0]


Q = Queue()
Q.enqueue('execute')

print(Q.dequeue())