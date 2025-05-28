class Myclass:
    def __init__(self):
        self.public_attribute = "public 속성"
        self.__privatte_attribute = "private 속성"
    def public_method(self):  # public 멤버, 어떤 클래스든 접근 가능
        print("public 메소드")
    def __private_method(self): # private 멤버, 오직 Myclass 내부에서만 접근 가능
        print("private 메소드")

    def access_private_members(self):
        self.__private_method()
        print(self.__privatte_attribute)


a = Myclass()

a.access_private_members()
