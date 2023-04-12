set1 = {1, 2, 5, 7, 8, 3}
set2 = {3, 5, 7, 8, 4, 2}


# Написати функцію, яка повертає тільки однакові елементи двох множин

def same_elements(set1: set, set2: set) -> set:
    return set1.intersection(set2)


# Написати функцію, яка повертає тільки унікальні елементи двох множин.

def unique_elements(set1: set, set2: set) -> set:
    return set1.symmetric_difference(set2)


print(f"Однакові елементи {same_elements(set1, set2)}")
print(f"унікальні елементи {unique_elements(set1, set2)}")
