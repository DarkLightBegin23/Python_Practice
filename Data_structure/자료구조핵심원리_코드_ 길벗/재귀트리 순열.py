def permutation(arr, start):
    if len(arr)-1 == start:  # 기저 사례 : start가 집합의 마지막 원소에 도달했을 때 섞을 다른 원소가 없으므로 완성된 순열 출력
        print(arr)
        return
    for idx in range(start, len(arr)):
        arr[start], arr[idx] = arr[idx], arr[start]
        permutation(arr, start+1) 
        '''
        집합 크기를 줄여서(start를 한 칸 움직여서) 다시 재귀함수 호출
        '''
        arr[start], arr[idx] = arr[idx], arr[start]  # 다시 자신의 스택 프레임으로 돌아왔다면 이전에 바꾸어 놓았던 원소를 다시 원래대로 돌려놓기

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    permutation(arr, 0)
