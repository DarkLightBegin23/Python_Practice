nums = [int(input()) for n in range(10) if n > 0 and n < 100]

max_value = max(nums)
number_index = nums.index(max_value)

print(max_value)
print(number_index + 1)