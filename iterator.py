# 사용자 정의 반복자 클래스 정의
class MyIterator:
    # 생성자: 클래스가 초기화될 때 호출됨
    def __init__(self, data):
        self.data = data        # 반복할 데이터(리스트 등)를 저장
        self.position = 0       # 현재 위치를 나타내는 인덱스, 처음에는 0으로 초기화

    # __iter__ 메서드: 반복 가능한 객체라는 것을 알려줌
    def __iter__(self):
        return self             # 자기 자신을 반복자(iterator)로 반환

    # __next__ 메서드: 다음 값을 반환하거나, 끝에 도달하면 StopIteration 예외를 발생시킴
    def __next__(self):
        if self.position >= len(self.data):  # 데이터의 끝에 도달했는지 확인
            raise StopIteration              # 더 이상 반환할 값이 없으면 반복 종료
        result = self.data[self.position]    # 현재 위치의 값을 가져옴
        self.position += 1                   # 위치를 다음으로 이동
        return result                        # 현재 값을 반환

# 이 파일이 직접 실행될 때만 아래 코드를 실행함 (다른 파일에서 import 될 때는 실행되지 않음)
if __name__ == "__main__":
    # MyItertor 클래스의 인스턴스를 생성 (리스트 [1, 2, 3, 4]를 반복할 수 있도록 함)
    i = MyIterator([1, 2, 3, 4])

    # for 루프를 통해 반복자를 순회하면서 각 요소를 출력
    for item in i:
        print(item)
