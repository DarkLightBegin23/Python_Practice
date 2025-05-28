class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.position = len(self.data) - 1
        
    def __iter__(self):
        return self
    
def __next__(self):
    '''
    현재 위치가 0보다 작으면, 순회할 항목이 더 이상 없다는 뜻이므로
    # StopIteration 예외를 발생시켜 반복을 종료합니다.
    # 이는 파이썬의 이터레이터 프로토콜에 따라 필수입니다.
    '''
    if self.position < 0:
        raise StopIteration  # 반복이 끝났음을 알리는 예외. for문 등에서 이 예외를 받아 종료하게 됩니다.

    # 현재 위치에 있는 데이터를 result에 저장합니다.
    result = self.data[self.position]

    # 다음 호출을 위해 위치를 하나 줄입니다 (역순 순회를 위함).
    self.position -= 1

    # 현재 위치의 데이터를 반환합니다.
    return result

    
if __name__ == "__main__":
    i = ReverseIterator([1, 2, 3])
    for item in i:
        print(item)