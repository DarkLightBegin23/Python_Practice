# 3052번 나머지

nums = [int(input()) for su in range(10)]
nums_re = []
for i in range(len(nums)):
    div = nums[i] % 42
    nums_re.append(div)

n = set(nums_re)

print(len(n))
