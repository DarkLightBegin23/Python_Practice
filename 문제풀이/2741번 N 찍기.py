nums = int(input())
nums_list = []
for i in range(nums):
    nums_list.append(i + 1)
    i -= 1

for j in nums_list:
    print(j)