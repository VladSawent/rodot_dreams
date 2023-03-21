# по кожному надрукованому символу
message = str(input("Please print message :"))

for token in list(message):
    if token == " ":
        print("  пробіл")
    elif token.isdigit():  # якщо число
        if int(token) % 2 == 0:
            print(token, "це парне число")
        else:
            print(token, "не парене число")
    elif token.isalpha():  # якщо буква
        if token.islower():
            print(token, "маленька літера")
        else:
            print(token, "велика літера")
    else:
        print(token, "Символ")  # виводить символ
