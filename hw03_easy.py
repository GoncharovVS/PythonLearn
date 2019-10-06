__author__ = "Гончаров Всеволод Сергеевич"

while True:
    print("Введи номер задачи (1-2) или 0 для выхода")
    key = int(input())

    # Задание-1:
    # Напишите функцию, округляющую полученное произвольное десятичное число
    # до кол-ва знаков (кол-во знаков передается вторым аргументом).
    # Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
    # Для решения задачи не используйте встроенные функции и функции из модуля math.

    if key == 1:

        def my_round(number, ndigits):
            factor = 1
            for _ in range(ndigits):
                factor *= 10
            number *= factor
            if number % 1 > 0.5:
                number += 1
            return int(number) / factor


        print(my_round(2.1234567, 5))
        print(my_round(2.1999967, 5))
        print(my_round(2.9999967, 5))

    # Задание-2:
    # Дан шестизначный номер билета. Определить, является ли билет счастливым.
    # Решение реализовать в виде функции.
    # Билет считается счастливым, если сумма его первых и последних цифр равны.
    # !!!P.S.: функция не должна НИЧЕГО print'ить

    elif key == 2:

        def lucky_ticket(ticket_number):

            ticket_number = str(ticket_number)
            ticket_number_list = []
            for symbol in ticket_number:
                ticket_number_list.append(int(symbol))

            sum1 = 0
            sum2 = 0
            i = 0
            while i < int(len(ticket_number_list) / 2):
                i += 1
                sum1 += ticket_number_list[i-1]
                sum2 += ticket_number_list[-i]

            return sum1 == sum2


        print(lucky_ticket(123006))
        print(lucky_ticket(12321))
        print(lucky_ticket(436751))
        print(lucky_ticket(1234))

    elif key == 0:
        break
    else:
        print("Ввел что-то не то, попробуй ещё раз")
