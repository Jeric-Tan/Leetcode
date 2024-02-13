s = "racecar"
n = len(s)
output = 0
#if odd number of letters
if n % 2 != 0:
    dp = [1] * (n//2)
    middle = n//2
    for i in range(1,middle):
        if s[middle-i] == s[middle+i]:
            output += 1
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            break
    

#if even number of letters
else:
    pass

print(output)