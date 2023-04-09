# Вивести всі елементу списку, які є числом, використовуючи filter.
seq = ["asery", "1", "as", "3", "4", "5"]


def list_n(list1):
    return list1.isdigit()


a = list(filter(list_n, seq))
print(a)
