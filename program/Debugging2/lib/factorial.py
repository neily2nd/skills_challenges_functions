def factorial(n):
    product = 1
    while n > 0:
        n -= 1
        product *= n
    return product


print(factorial(5))
