class FourCal: #클래스 Fourcal 생성
    def __init__(self, first, second): # 초기화 메서드 추가
        self.first = first
        self.second = second
    def setdata(self, first, second): #메서드(클래스 안에 구현된 함수)의 매개변수
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
a = FourCal() #객체 a 정의
b = FourCal() #객체 b 정의

one = int(input("첫번째 숫자:"))
two = int(input("두번째 숫자:"))
three = int(input("세번째 숫자:"))
four = int(input("네번째 숫자:"))

a.setdata(one, two)
b.setdata(three, four)

a.add()
a.mul()
a.sub()
a.div()
b.add()
b.mul()
b.sub()
b.div()

c = [a.add(), a.mul(), a.sub(), a.div(), b.add(), b.mul(), b.sub(), b.div()]

for i in c:
    print(i)