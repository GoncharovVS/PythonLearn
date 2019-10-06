__author__ = "Гончаров Всеволод Сергеевич"

import random
import math

while True:
    print("Введи номер задачи (1-4) или 0 для выхода")
    key = int(input())

    # Задание-1:
    # Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
    # Первыми элементами ряда считать цифры 1 1

    if key == 1:

        def fibonacci(n, m):
            answer = [1, 1]
            i = 2

            while i < m:
                answer.append(answer[i-1] + answer[i-2])
                i += 1

            return answer[n-1:]

        print(fibonacci(1, 6))
        print(fibonacci(5, 9))
        print(fibonacci(38, 40))

    # Задача-2:
    # Напишите функцию, сортирующую принимаемый список по возрастанию.
    # Для сортировки используйте любой алгоритм (например пузырьковый).
    # Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

    elif key == 2:

        def sort_to_max(origin_list):
            if len(origin_list) <= 2:
                return origin_list
            else:
                key_item = random.choice(origin_list)
                a_list = []
                b_list = []
                c_list = []
                for item in origin_list:
                    if item < key_item:
                        a_list.append(item)
                    elif item > key_item:
                        b_list.append(item)
                    else:
                        c_list.append(item)
                return sort_to_max(a_list) + c_list + sort_to_max(b_list)

        print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

    # Задача-3:
    # Напишите собственную реализацию стандартной функции filter.
    # Разумеется, внутри нельзя использовать саму функцию filter.

    elif key == 3:

        def custom_filter(func, original_list):
            answer = []
            for item in original_list:
                if func(item):
                    answer.append(item)
            return answer


        print(custom_filter(lambda x: x > 0, [-2, -1, 0, 1, 2]))

    # Задача-4:
    # Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
    # Определить, будут ли они вершинами параллелограмма.

    elif key == 4:

        def it_is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4):

            len_1_2 = len_line(x1, y1, x2, y2)
            len_1_3 = len_line(x1, y1, x3, y3)
            len_1_4 = len_line(x1, y1, x4, y4)
            len_2_3 = len_line(x2, y2, x3, y3)
            len_2_4 = len_line(x2, y2, x4, y4)
            len_3_4 = len_line(x3, y3, x4, y4)

            if len_1_2 == len_3_4 and (len_1_3 == len_2_4 or len_1_4 == len_2_3):
                return True
            else:
                return False

        def len_line(x1, y1, x2, y2):
            return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

        x1 = 1
        y1 = 3
        x2 = 4
        y2 = 7
        x3 = 2
        y3 = 8
        x4 = -1
        y4 = 4
        print(it_is_parallelogram(x1, y1, x2, y2, x3, y3, x4, y4))

    elif key == 0:
        break
    else:
        print("Ввел что-то не то, попробуй ещё раз")
