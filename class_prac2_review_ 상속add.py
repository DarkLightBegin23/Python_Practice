
'''
class Sub:
    def __init__(self, one, two):
        self.one = one
        self.two = two
    def Subs(self):
        result = self.one * self.two
        return result
    
class div(Sub):
    def __init__(self, three, four):
        self.three = three
        self.four = four
    def divi(self):
        result2 = self.three / self.four
        return result2
    

print(Sub(2, 5))
print(div(3, 4))

'''

class Sub:
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def Subs(self):
        result = self.one * self.two
        return result
    
class div(Sub):
    def __init__(self, one, two, three, four):
        super().__init__(one, two)  # 부모 클래스의 생성자 호출
        self.three = three
        self.four = four

    def divi(self):
        result2 = self.three / self.four
        return result2

# 객체 생성 후 메서드 호출
sub_instance = Sub(2, 5)
print(sub_instance.Subs())  # 10 출력

div_instance = div(2, 5, 3, 4)
print(div_instance.Subs())  # 부모 클래스의 메서드 호출 -> 10 출력
print(div_instance.divi())  # 자식 클래스의 메서드 호출 -> 0.75 출력

# 복습하기!! (202400822)