class Flight:
    def __init__(self, number):
        self._number = number
    
    
    def number(self):
        return self._number
    
# 인스턴스 생성
f = Flight('KE2349')
print(f.number())