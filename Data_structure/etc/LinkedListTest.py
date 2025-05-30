class Node:
    def __init__(self, data):
        self.data = data  # 노드가 저장할 데이터
        self.next = None  # 다음 노드를 가리키는 포인터 (초기에는 None)
        
class LinkedList:
    def __init__(self):
        self.head = None  # 연결 리스트의 첫 번째 노드
        
    def append(self, data):
        if not self.head:
            self.head = Node(data)  # head 없으요 -> head를 새 노드로 설정
        else:  # 비어있지 않다?
            current = self.head  # current를 head부터  시작해서
            while current.next:  # .next가 None인 마지막 노드를 찾음(밑)
                current = current.next  # current.next가 존재하지 않을 때까지 next를 함.
            current.next = Node(data)  # 마지막 노드의 .next에 새 노드 연결
            
    def print_list(self):
        current = self.head  
        while current:  # current가 None이 될 때까지 반복
            print(current.data)
            current = current.next
            
    
if __name__ == "__main__":
    linked_list = LinkedList()
    
    linked_list.append(input("1번째 요소 : "))
    linked_list.append(input("2번째 요소 : "))
    linked_list.append(input("3번째 요소 : "))
    
    
    linked_list.print_list()