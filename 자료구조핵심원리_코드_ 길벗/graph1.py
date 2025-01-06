class Graph:
    def __init__(self, vertex_num=None):
        # 인접 리스트
        self.adj_list = []
        self.vtx_num = 0
        # 정점이 있다면 True
        # 정점이 없다면 False
        self.vtx_arr = []
        # 정점 개수를 매개변수로 넘기면 초기화 진행
        
        if vertex_num:
            self.vtx_num = vertex_num
            self.vtx_arr = [True for _ in range(self.vtx_num)]
            self.adj_list = [[] for _ in range(self.vtx_num)]