# сумує будь-яку кількість аргументів

def adder(*nums):
    a = 0

    for n in nums:
        a += n

    print("Сума=", a)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)
