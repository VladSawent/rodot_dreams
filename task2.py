#Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі, використовуючи рекурсію
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)   #xn = xn−1 + xn−2


print(fibonacci(3))
print(fibonacci(6))
print(fibonacci(9))
