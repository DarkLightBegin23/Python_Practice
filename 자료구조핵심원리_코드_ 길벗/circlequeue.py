class CQueue:
    MAXSIZE = 10
    def __init__(self):
        self.container = [None for _ in range(CQueue.MAXSIZE)]
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False
    
    def __step_forward(self, x):
        x += 1
        if x >= CQueue.MAXSIZE:
            x = 0
        return x

    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.container[self.rear] = data
        self.rear = self.__step_forward(self.rear)  # rear는 마지막 데이터의 다음을 가리킴

    def dequeue(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        ret = self.container[self.front]
        self.front = self.__step_forward(self.front)
        return ret

    def peek(self):
        if self.is_empty():
            raise Exception('The queue is empty')
        return self.container[self.front]


cq = CQueue()

for i in range(9):
    cq.enqueue(i)

for i in range(5):
    print(cq.dequeue(), end = " ")

try:
    for i in range(8, 14):
        cq.enqueue(i)
except Exception as e:
    print(e)

while not cq.is_empty():
    print(cq.dequeue(), end = " ")

print()

for i in range(10):
    print(cq.container[i], end = ' ')

