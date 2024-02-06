#Group Anagrams
strs = ["eat","tea","tan","ate","nat","bat"]

ana_groups = {}
output = []
for word in strs:
    key = "".join(sorted(word))
    
    if key in ana_groups:
        ana_groups[key] += [word] 
        
    else:
        ana_groups[key] = [word]
    print(ana_groups)
    
print(list(ana_groups.values()))
    
    
    
    
    

