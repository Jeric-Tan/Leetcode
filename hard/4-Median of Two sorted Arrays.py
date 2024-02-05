import math
#Expected [0, 1, 2, 4, 5, 3]
nums1 = [1,3]
nums2 = [2]

ans = nums1 + nums2
ans = sorted(ans)
left = ans[int(math.floor(len(ans)/2))]
if len(ans) % 2 == 0 and left >= 1:
    left = ans[int(math.floor(len(ans)/2)) - 1]
right = ans[int(math.floor(len(ans)/2))]

print((left+right)/2.0)