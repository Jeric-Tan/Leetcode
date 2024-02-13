#647 - Palindromic Substrings
s = "aaa"
n = len(s)
output = 0
for i in range(n):
    l=r=i
    while l >= 0 and r < n and s[l] == s[r]:
        output += 1
        l -= 1
        r += 1
    
    l = i 
    r = i + 1
    while l >= 0 and r < n and s[l] == s[r]:
        output += 1
        l -= 1
        r += 1
print(output)
