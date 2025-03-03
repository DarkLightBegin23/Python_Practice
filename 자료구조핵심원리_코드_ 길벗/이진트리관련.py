class TreeNode:
    def __init__(self, data=None):
        self.__data = data
        self.__left = None
        self.__right = None
        
    def __del__(self):
        print('data {} is deleted'.format(self.__data))
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
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
    # 현재 노드가 empty node라면
    if not cur:
        return
    
    # 방문
    print(cur.data, end = ' ')
    
    preorder(cur.left)  # 왼쪽 서브 트리로 이동
    
    preorder(cur.right)  # 오른쪽 서브 트리로 이동
    
    
if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7
    
    preorder(n1)
    print()