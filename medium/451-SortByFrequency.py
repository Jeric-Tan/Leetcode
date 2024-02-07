#Sort characters By Frequency

s = "tree"
output = ''
s_dict = {}
for letter in s:
    if letter not in s_dict:
        s_dict[letter] = 1
    else:
        s_dict[letter] += 1

x = sorted(s_dict.items(), key=lambda item: item[1], reverse=True)
for pair in x:
    for i in range(pair[1]):
        output += pair[0]
        
print(output)