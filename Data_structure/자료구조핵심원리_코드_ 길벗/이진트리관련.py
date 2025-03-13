class TreeNode:
    def __init__(self, data=None):
        """
        이진 트리의 노드를 정의하는 클래스
        :param data: 노드에 저장될 데이터
        """
        self.__data = data  # 노드의 데이터
        self.__left = None  # 왼쪽 자식 노드
        self.__right = None  # 오른쪽 자식 노드
        
    def __del__(self):
        """
        객체가 소멸될 때 호출되는 소멸자
        """
        print('data {} is deleted'.format(self.__data))
        
    @property    # getter
    def data(self):
        return self.__data
    
    @data.setter   # setter
    def data(self, data):
        self.__data = data
        
    @property  
    def left(self):
        return self.__left
    
    @left.setter 
    def left(self, left):
        self.__left = left
        
    @property
    def right(self):
        return self.__right
    
    @right.setter
    def right(self, right):
        self.__right = right


def preorder(cur):
    """
    전위 순회(Preorder Traversal) 함수
    :param cur: 현재 방문하는 노드
    """
    # 현재 노드가 존재하지 않으면 종료
    if not cur:
        return
    
    # 현재 노드의 데이터 출력 (방문)
    print(cur.data, end=' ')
    
    # 왼쪽 서브트리 방문
    preorder(cur.left)
    
    # 오른쪽 서브트리 방문
    preorder(cur.right)
    
    
if __name__ == "__main__":
    # 이진 트리 노드 생성
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    
    # 트리 구조 설정
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7
    
    # 전위 순회 실행
    preorder(n1)
    print()
