# bookstore(왕초보를 위한 파이썬)

class Book:
    def __init__(self):
        self.title = input("책의 제목 :")
        self.price = int(input("책의 가격 :"))
        self.author = input("책의 저자 :")
        self.소장 = "왕초보서점"
    
    def printData(self):
        print("==== 책 ====")
        print("제목 :",self.title)
        print("가격 :",self.price)
        print("저자 :",self.author)
        print("소장 :",self.소장)
    
    def __str__(self):
        return f"책이 들어왔습니다. {self.title} / {self.price} / {self.author}"

book1 = Book()
print(book1)  # __str__
print(book1.printData())