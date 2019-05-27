fibonacci_cache = {}

def fibonacci(n):
    """Fibonacci sequence function"""
    if n in fibonacci_cache:        # improved fibonacci
        return fibonacci_cache[n]
    elif n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the value and return it
    fibonacci_cache[n] = value
    return value

for l in range(1,10):
    print(l, ":", fibonacci(l))

try:
    print(fibonacci(2.1))
except UnboundLocalError:
    print("The input is incorect type")
