from functools import lru_cache

@lru_cache(maxsize = 10000)
def fibonacci(n):
    if n == 1:
        return  1
    elif n == 2:
        return  1
    elif n > 2:
        return  fibonacci(n-1) + fibonacci(n-2)

for l in range(1, 20):
    print(l, ":", fibonacci(l))

try:
    print(fibonacci(2.1))
except TypeError:
    print("The input is incorect type")
