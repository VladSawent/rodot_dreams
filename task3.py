# Перетворити всі елементи списку типу string в верхній регістр, використовуючи map
a = ['vxcsd', 'wdf', 'sdf', 'fgh', 'qweq', 'rty']


def up(list_str):
    return list_str.upper()


b = list(map(up, a))
print(b)
