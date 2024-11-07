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
