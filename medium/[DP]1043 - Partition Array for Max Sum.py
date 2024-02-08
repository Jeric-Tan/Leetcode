#DP problem! 
#Partition Array for Maximum Sum

class Solution(object):

    def maxSumAfterPartitioning(self, arr, k):
        memo = {}
        def solve(i):
            if i == len(arr):
                return 0
            
            if i in memo:
                return memo[i]
        
            max_value = 0
            ans = 0
            for j in range(i,min(i+k,len(arr))):
                max_value = max(max_value, arr[j])
                ans = max(ans, max_value * (j-i+1) + solve(j+1))
            memo[i] = ans
            return ans
        return solve(0)

