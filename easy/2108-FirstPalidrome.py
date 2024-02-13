#2108 Find First Palidromic String in the Array
#Easy
words = ["abc","car","ada","racecar","cool"]

def palidrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

print(palidrome(words))