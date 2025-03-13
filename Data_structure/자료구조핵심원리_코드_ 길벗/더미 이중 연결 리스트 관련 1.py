class Node:
    def __init__(self, data=None):
        # 데이터를 담고 있는 노드 초기화
        self.__data = data     # __data는 외부에서 직접 접근할 수 없도록 보호된 변수
        self.__prev = None     # 이전 노드를 가리키는 포인터
        self.__next = None     # 다음 노드를 가리키는 포인터
    
    # 소멸자 : 객체가 사라지기 전 호출됨
    # 삭제 연산 시 데이터 삭제 확인용 출력
    def __del__(self):
        print("data of {} is deleted".format(self.data))

    # @property 데코레이터는 data 변수를 읽기 전용 속성으로 만들어 줌
    @property
    def data(self):
        # __data 변수의 값을 반환하는 getter 메서드
        return self.__data
    
    # @data.setter는 data 변수에 값을 설정할 수 있는 setter 메서드를 정의
    @data.setter
    def data(self, data):
        self.__data = data     # __data에 새로운 값을 설정
    
    # prev 변수의 getter 메서드로, 노드의 이전 포인터 반환
    @property
    def prev(self):
        return self.__prev
    
    # prev 변수의 setter 메서드로, 이전 포인터를 설정할 수 있음
    @prev.setter
    def prev(self, p):
        self.__prev = p

    # next 변수의 getter 메서드로, 노드의 다음 포인터 반환
    @property
    def next(self):
        return self.__next
    
    # next 변수의 setter 메서드로, 다음 포인터를 설정할 수 있음
    @next.setter
    def next(self, n):
        self.__next = n

class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를 저장하지 않은 노드(== 더미 노드)
        self.head = Node()
        self.tail = Node()
        # 초기화
        # head와 tail 연결
        self.head.next = self.tail
        self.tail.prev = self.head
        # 데이터의 개수를 저장할 변수
        self.d_size = 0
    
    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False
    def size(self):
        return self.d_size
    
    def add_first(self, data):
        new_node = Node(data)  # 새 데이터를 담을 새 노드 생성
        new_node.next = self.head.next  # 새 노드의 next는 기존 첫 번째 노드를 가리킴
        new_node.prev = self.head       # 새 노드의 prev는 리스트의 head(더미 노드)를 가리킴

        # 기존 첫 번째 노드의 prev를 새 노드로 설정해 연결을 갱신
        self.head.next.prev = new_node  
        # 더미 노드(head)의 next를 새 노드로 갱신하여 연결
        self.head.next = new_node       

        # 데이터 개수 증가
        self.d_size += 1  

    def add_last(self, data):
        new_node = Node(data)  # 새 데이터를 담을 새 노드 생성 
        # 새 노드의 prev는 리스트의 마지막 데이터 노드를 가리킴
        new_node.prev = self.tail.prev  
        # 새 노드의 next는 tail(더미 노드)을 가리킴
        new_node.next = self.tail       

        # 기존 마지막 데이터 노드의 next를 새 노드로 설정
        self.tail.prev.next = new_node  
        # tail(더미 노드)의 prev를 새 노드로 설정하여 연결
        self.tail.prev = new_node       

        # 데이터 개수 증가
        self.d_size += 1  

    def insert_after(self, data, node):
        new_node = Node(data)  # 새 데이터를 담을 새 노드 생성
        new_node.next = node.next  # 새 노드의 next는 삽입할 위치의 다음 노드를 가리킴
        new_node.prev = node       # 새 노드의 prev는 현재 노드를 가리킴

        # 현재 노드의 다음 노드의 prev를 새 노드로 설정
        node.next.prev = new_node  
        # 현재 노드의 next를 새 노드로 설정하여 삽입 완료
        node.next = new_node       

        # 데이터 개수 증가
        self.d_size += 1  

    def insert_before(self, data, node):
        new_node = Node(data)  # 새 데이터를 담을 새 노드 생성
        
        # 새 노드의 prev는 삽입할 위치의 이전 노드를 가리킴
        new_node.prev = node.prev  
        # 새 노드의 next는 현재 노드를 가리킴
        new_node.next = node       

        # 현재 노드의 이전 노드의 next를 새 노드로 설정
        node.prev.next = new_node  
        # 현재 노드의 prev를 새 노드로 설정하여 삽입 완료
        node.prev = new_node       

        # 데이터 개수 증가
        self.d_size += 1  
    
    def search_forward(self, target):
        cur = self.head.next
        # 데이터 노드를 순회할 cur 변수 : 첫 번째 데이터 노드부터 시작하므로 self.head.next를 가리킴
        
        while cur is not self.tail:  # 리스트의 마지막 노드가 더미 노드이므로 더미 노드가 아니라면 아직 데이터 노드입니다.
            if cur.data == target:
                return cur
            cur = cur.next
        return None
    
    def search_backward(self, target):
        cur = self.tail.prev
        while cur is not self.head:
            if cur.data == target:
                return cur
            cur = cur.prev
        return None
    
    def delete_first(self):
        if self.empty():
            return
        self.head.next = self.head.next.next
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_ndoe(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1
        