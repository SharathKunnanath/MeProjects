def fibIter(n):
    memo = {0: 0, 1: 1}
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n] 

#Testing
print(f'The Fibonacci number for 0 is {fibIter(0)}')
print(f'The Fibonacci number for 1 is {fibIter(1)}')
print(f'The Fibonacci number for 5 is {fibIter(5)}')
print(f'The Fibonacci number for 10 is {fibIter(10)}')
print(f'The Fibonacci number for 50 is {fibIter(50)}')