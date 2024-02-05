#Convert an Array into a 2D array with conditions 

nums = [1,3,4,1,2,3,1]

dict_nums = {}
output = []
create_list = True
for i in nums:
    if i not in dict_nums:
        dict_nums[i] = 1
    else:
        dict_nums[i] += 1

print(max(dict_nums, key = dict_nums.get))
print(dict_nums[(max(dict_nums, key = dict_nums.get))])

for i in range(dict_nums[(max(dict_nums, key = dict_nums.get))]):
    x = []
    for key in dict_nums:
        if dict_nums[key] > 0:
            x.append(key)
            dict_nums[key] -= 1
    output.append(x)
    
print(output)