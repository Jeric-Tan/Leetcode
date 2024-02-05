#Divide Array into Arrays With Max Difference

numberss = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,3,12,12,2,13,2,2]

def divideArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    # 1 1 3 3 4 5 8 7 9
    nums.sort()
    output = []

    if len(nums)%3 != 0:
        return []

    i = 0
    for i in range((len(nums)//3)):

        if  nums[2] - nums[0] <= k:
            output.append(nums[0:3])
            print("start:", nums, len(nums))
            nums.pop(0)
            nums.pop(0)
            nums.pop(0)
            print("end", nums, len(nums))
        else:
            return []
    return output
        
print(divideArray(numberss, 2))