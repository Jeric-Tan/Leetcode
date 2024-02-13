#Least number of perfects squares that add up the given number

memo = {}
n=12
squares = []
i = 1
while (i**2) <= n:
    squares.append(i**2)
    i += 1 

def solve(i):
    print("Solving: ", i)
    steps = 0
    
    if i == 0:
        print("returned value: 0")
        return steps
    
    if i in memo:
        return memo[i]
    

    arr = squares
    #[1,4] len = 4
    for j in range(len(arr)):
        if arr[j] <= i:
            temp_steps = 1 + min(i, solve(i-arr[j]))
            if temp_steps < steps or steps == 0:
                steps = temp_steps

    print("returned value: ", steps,"\n")
    memo[i] = steps
    return steps

solve(n)
print(memo)