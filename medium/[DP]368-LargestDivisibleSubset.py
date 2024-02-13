# 368 DYNAMIC Programming 
# Largest Divisible Subset
nums = [3,4,16,8,7]

def LDS(nums):
    nums.sort()
    dp = [1] * len(nums)
    max_size = 1
    max_index = 0
    
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] > max_size:
                    max_size = dp[i]
                    max_index = i
                    
    array = []
    num = nums[max_index]
    for i in range(max_index, -1, -1):
        if num % nums[i] == 0 and dp[i] == max_size:
            array.append(nums[i])
            num = nums[i]
            max_size -= 1


    return max_size, max_index, dp, array[::-1]
                
print(LDS(nums))
