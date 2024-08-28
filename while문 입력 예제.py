prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number : """

number = 0                  # 'Enter number' 에서 보다시피 number는 번호 입력 받을 변수!
while number != 4:            # 입력받은 번호가 4가 아닌 동안에는 반복
    print(prompt)
    number = int(input())
    
