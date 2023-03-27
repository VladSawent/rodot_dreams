# Знайти найбільший елемент масиву
t = [1, 34, 1, 3]
print(f"Максимальне значення {max(t)}")


def max_element(a):
    max_num = 0
    for i in a:
        if i > max_num:
            max_num = i
    print(f"Максимальне значення {max_num}")


max_element(a=[1, 34, 65, 3])
