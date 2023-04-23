# Написати рекурсію, яка буде друкувати числа від введенного користувачем до нуля.

def recursion(i: int):
    print(i, end=" ")
    if i == 0:  # Вихід з рекурсії
        return None

    return recursion(i - 1)  # умова рекурсії


n = int(input("Напишіть число для рекурсії :"))
recursion(n)
