#Remove Element
#Notes: Tried the swapping method

nums =[4,5]
val = 5

k = 0
end_ptr = len(nums)-1
start_ptr = 0

while start_ptr < end_ptr:
    if nums[end_ptr] == val:
        end_ptr -= 1

    if nums[start_ptr] == val and nums[end_ptr] != val:
        temp = nums[start_ptr]
        nums[start_ptr] = nums[end_ptr]
        nums[end_ptr] = temp
        end_ptr -= 1
        
    if nums[start_ptr] != val:
        start_ptr += 1    
for num in nums:
    if num != val:
        k += 1

print(nums, k)