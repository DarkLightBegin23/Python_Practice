a = int(input())
b = input()

b_list = list(map(int, str(b))) # b는 문자열이니 정수형으로 변환 후 각각의 자리를 리스트로 변환
b_int = int(b)

for i in reversed(b_list):  # reversed(b_list) ==> 리스트 요소들을 거꾸로 꺼내서 반복
    print(a * i)
print(a * b_int)