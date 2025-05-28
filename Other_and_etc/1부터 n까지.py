def sumNumber():
    i = 0
    sum = 0
    
    n = int(input())
    
    while i < n:
        i += 1
        sum += i
    
    return sum

if __name__ == "__main__":
    a = sumNumber()
    print(f'총 합 : {a}')