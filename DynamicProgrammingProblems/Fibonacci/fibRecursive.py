memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

#Testing
print(f'The Fibonacci number for 0 is {fib(0)}')
print(f'The Fibonacci number for 1 is {fib(1)}')
print(f'The Fibonacci number for 5 is {fib(5)}')
print(f'The Fibonacci number for 10 is {fib(10)}')
print(f'The Fibonacci number for 50 is {fib(50)}')
