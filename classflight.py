class Flight:
    def __init__(self, number):
        self._number = number
    
    def number(self):
        return self._number  # 인스턴스 변수 반환
    
    def updateNumber(self, num):
        self._number = num
        return self._number

# 인스턴스 생성
f = Flight('KE2349')
f.updateNumber("KE3485")
print(f.number())