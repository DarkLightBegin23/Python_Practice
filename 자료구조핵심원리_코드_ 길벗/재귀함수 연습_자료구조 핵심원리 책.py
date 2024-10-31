def factorial(n):
    # base case(기저 사례 - 재귀 함수 호출을 멈추는 특정 조건)
    if n <= 0:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    for i in range(1, 8):
        print(factorial(i))
