password = "vabos123"
attempts = 3

while attempts > 0:
    guess = input("Введи пароль: ")
    if guess == password:
        print("Верно! Добро пожаловать!")
        break
    else:
        attempts = attempts - 1
        print(f"Неверно! Осталось попыток: {attempts}")

if attempts == 0:
    print("Доступ закрыт!")