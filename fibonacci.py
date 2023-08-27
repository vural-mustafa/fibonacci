def fibonacci(n):
    fib_series = [0, 1] 

    for i in range(2, n):
        next_fib = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_fib)

    return fib_series

n = int(input("Fibonacci dizisi kaç elemanlı olmalı? "))
result = fibonacci(n)
print(result)
