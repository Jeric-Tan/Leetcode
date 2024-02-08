#Rotate array

nums = [1,2]
k = 3
k = k % len(nums)
output = []
output = nums[-k:]

nums = output + nums[:-k]


print(nums)