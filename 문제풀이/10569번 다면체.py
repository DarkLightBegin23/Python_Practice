# 10569번 다면체
T = int(input())

for i in range(T):
    V, E = map(int, input().split())

    face = 2 - V + E 
    '''
     (꼭짓점의 수) - (모서리의 수) + (면의 수) = 2
     (면의 수) = 2 - (꼭짓점의 수) + (모서리의 수)
    '''
    print(face)