__author__ = "Гончаров Всеволод Сергеевич"

import re
import os

while True:
    print("Введи номер задачи (1-3) или 0 для выхода")
    key = int(input())

    # Задание-1:
    # Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
    # Дроби вводятся и выводятся в формате:
    # n x/y ,где n - целая часть, x - числитель, у - знаменатель.
    # Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
    # Примеры:
    # Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
    # Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
    # Ввод: -2/3 - -2
    # Вывод: 1 1/3

    if key == 1:

        def parse(value):

            pattern = re.compile(r"(.+)( [+\-*/] )(.+)")
            result = pattern.findall(value)
            value1, action, value2 = result.pop()
            integer1, numerator1, denumerator1 = parseNum(value1)
            integer2, numerator2, denumerator2 = parseNum(value2)
            action = re.sub(" ", "", action)

            return action, int(integer1), int(numerator1), int(denumerator1), int(integer2), int(numerator2), int(denumerator2)


        def parseNum(number):

            integer = 0
            numerator = 1
            denumerator = 1

            if re.search(r'\d+ \d+/\d+', number):
                for idx2, item2 in enumerate(re.findall(r'(\d+) (\d+)/(\d+)', number).pop(), start=1):
                    if idx2 == 1:
                        integer = item2
                    elif idx2 == 2:
                        numerator = item2
                    else:
                        denumerator = item2
            elif re.search(r'\d+/\d+', number):
                for idx2, item2 in enumerate(re.findall(r'(\d+)/(\d+)', number).pop(), start=1):
                    if idx2 == 1:
                        numerator = item2
                    else:
                        denumerator = item2
            elif re.search(r'\d+'):
                integer = re.findall(r'(\d+)', number).pop()

            return integer, numerator, denumerator


        def goToComDenom(nom1, nom2, denom1, denom2):
            max = denom1 if denom1 > denom2 else denom2
            denom1 * denom2
            for i in range(denom1 * denom2 + 1):
                if (i + max) % denom1 == 0 and (i + max) % denom2 == 0:
                    nom1 *= (i + max) // denom1
                    nom2 *= (i + max) // denom2
                    return i + max, nom1, nom2


        def reduce(Nom, Denom):
            reduceComplete = False
            while reduceComplete == False:
                reduceComplete = True
                for i in range(Nom - 1):
                    if Nom % Nom - i == 0 and Denom % Nom - i == 0:
                        Nom /= Nom - i
                        Denom /= Nom - i
                        reduceComplete = False
            return Nom, Denom



        print("Введи пример с простыми дробями: ")
        value = input()
        act, int1, nom1, denom1, int2, nom2, denom2 = parse(value)

        nom1 += int1 * denom1
        nom2 += int2 * denom2

        if act == "+":
            Denom, nom1, nom2 = goToComDenom(nom1, nom2, denom1, denom2)
            Nom = nom1 + nom2
        elif act == "-":
            Denom, nom1, nom2 = goToComDenom(nom1, nom2, denom1, denom2)
            Nom = nom1 - nom2
        elif act == "*":
            Nom = nom1 * nom2
            Denom = denom1 * denom2
        elif act == "/":
            Nom = nom1 * denom2
            Denom = denom1 * nom2
        else:
            print("Не распознано действие")
            continue

        Int = Nom // Denom
        Nom -= Int * Denom
        Nom, Denom = reduce(Nom, Denom)
        if Nom == 0:
            print("Ответ: {}".format(Int))
        else:
            print("Ответ: {} {}/{}".format(Int, Nom, Denom))

    # Задание-2:
    # Дана ведомость расчета заработной платы (файл "data/workers").
    # Рассчитайте зарплату всех работников, зная что они получат полный оклад,
    # если отработают норму часов. Если же они отработали меньше нормы,
    # то их ЗП уменьшается пропорционально, а за заждый час переработки
    # они получают удвоенную ЗП, пропорциональную норме.
    # Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

    elif key == 2:

        workers = []
        path = os.path.join('data', 'workers.txt')
        pattern = re.compile(r'(\w+) +(\w+) +(\d+) +\w+ +(\d+)')
        with open(path, 'r', encoding="UTF-8") as f:
            for idx, line in enumerate(f.readlines()):
                worker_value = pattern.findall(line)
                if not worker_value == []:
                    name, surname, cost, norm = worker_value.pop()
                    workers.append({"name": name, "surname": surname,"cost": int(cost),"norm": int(norm)})

        path = os.path.join('data', 'hours_of.txt')
        pattern = re.compile(r'(\w+) +(\w+) +(\d+)')
        with open(path, 'r', encoding="UTF-8") as f:
            for idx, line in enumerate(f.readlines()):
                hours_value = pattern.findall(line)
                if not hours_value == []:
                    name, surname, hours = hours_value.pop()
                    for worker in workers:
                        if worker["name"] == name and worker["surname"] == surname:
                            worker["hours"] = int(hours)

        for worker in workers:
            off_hours = worker["hours"] - worker["norm"]
            if off_hours > 0:
                off_hours *= 2
            worker["money"] = round(worker["cost"] + ((worker["cost"] / worker["norm"]) * off_hours))

        for worker in workers:
            print("{} {}: Отработано {} часов, норма {}. Оклад {}, к выплате {}".
                  format(worker["name"], worker["surname"], worker["hours"], worker["norm"], worker["cost"], worker["money"]))

    # Задание-3:
    # Дан файл ("data/fruits") со списком фруктов.
    # Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
    # Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
    # Файлы назвать соответственно.
    # Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
    # Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
    # Напишите универсальный код, который будет работать с любым списком фруктов
    # и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
    # Подсказка:
    # Чтобы получить список больших букв русского алфавита:
    # print(list(map(chr, range(ord('А'), ord('Я')+1))))

    elif key == 3:

        fruits = []
        path = os.path.join('data', 'fruits.txt')
        with open(path, 'r', encoding="UTF-8") as f:
            for line in f.readlines():
                if line != "\n":
                    fruits.append(line)
        path = ""

        fruits.sort()
        rune = ""
        file_change = False
        for fruit in fruits:
            if fruit[:1] != rune:
                if file_change:
                    f.close()
                else:
                    file_change = True
                rune = fruit[:1]
                file_name = "fruits_{}.txt".format(rune)
                path = os.path.join('data', 'fruits', file_name)
                f = open(path, 'w', encoding='UTF-8')
            f.write(fruit + "\n")

    elif key == 0:
        break
    else:
        print("Ввел что-то не то, попробуй ещё раз")
