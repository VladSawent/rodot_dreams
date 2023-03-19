# повідомляти — чи є введений текст “числом” чи “словом”
message = str(input("Please print message :"))
if message == "":
    print("Немає значення =(")
elif message.isdigit():  # якщо число
    if int(message) % 2 == 0:
        print(message, "це парне число")
    else:
        print(message, "не парене число")
else:
    print("Довжина слова", len(message))  # виводить довжину строки
