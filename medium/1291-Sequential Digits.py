#Sequential Digits

low = 10000
high = 300000
output = []


def sequentialDigits(low, high):
    """
    :type low: int
    :type high: int
    :rtype: List[int]
    """
    output = []

    for i in range(1,10):
        num = i
        for j in range(i+1, 10):
            num = num*10 + j
        
            if low <= num and num <= high:
                print(num)
                output.append(num)
                print(output)
    return sorted(output)

print(sequentialDigits(low,high))