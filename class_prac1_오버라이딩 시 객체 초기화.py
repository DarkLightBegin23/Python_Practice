class FourCal: #클래스 Fourcal 생성
    def __init__(self, first, second): # 초기화 메서드 추가
        self.first = first
        self.second = second
        
    def setdata(self, first, second): #메서드(클래스 안에 구현된 함수)의 매개변수 / setdata 메서드 (초기화 역할)
        self.first = first # 메서드 수행문(self 객체에 객체변수 first 생성)
        self.second = second # 메서드 수행문(self 객체에 객체변수 second 생성)
    
    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second
        

# 객체 생성 시 __init__ 메서드가 자동으로 호출됨

a = SafeFourCal(4, 0)
a.div()
print(a.div())