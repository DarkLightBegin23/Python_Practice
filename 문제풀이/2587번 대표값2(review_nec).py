nums = [int(input()) for i in range(5)]
print(int(sum(nums) / 5))  # 평균(5개 값으로 평균을 구하니까) + 자연수로 나오게끔 'int'
print(sorted(nums)[2])  # 중앙값(3번째 요소가 nums[2])