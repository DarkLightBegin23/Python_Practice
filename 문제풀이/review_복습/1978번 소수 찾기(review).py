N = int(input())   # 몇 개의 수를 받을것인지 입력받는 N
L = list(map(int, input().split()))  # 테스트 케이스
prime = 0   # 소수 초기화

for num in L:
    if num == 1:  # 1은 소수가 아니므로 건너뜀
        continue
    for i in range(2, num):
        if (num % i == 0):  # num을 하나라도 나누는 약수가 있다면
            break  # 소수가 아니므로 break(검사 멈춤)
    else:  # 한 번도 나눠지지 않고 for문이 끝나면, else 실행(소수로 판정)
        prime += 1
        
print(prime)


'''
어떤 수 num이 소수일 시, num % i != 0 (단, i는 2 이상 num - 1 이하인 모든 수)
num이 만약 2부터 num-1 사이의 수로 나눠지면,
1과 자기 자신 외에도 약수가 존재하게 됨.
'''