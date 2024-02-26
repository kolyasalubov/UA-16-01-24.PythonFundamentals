from random import randint

guessed_number = randint(1,100)

i = 0

while True:
    user_number = int(input("Вгадай число від 1 до 100: "))

    if user_number == guessed_number:
        print("Вітаю, ти вгадав!")
        break
    elif user_number > guessed_number:
        print("Загадане число менше, спробуй ще раз!")
    elif user_number < guessed_number:
        print("Загадане число більше, спробуй ще раз!")
    i += 1
    if i >= 10:
        print("Всі спроби на жаль витрачені!")
        break