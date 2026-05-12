def fib(n) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)   # NOT print — return

def fibonacci(count) -> list:
    return [fib(i) for i in range(count)]

x = int(input("enter the number: "))
print(fibonacci(x))