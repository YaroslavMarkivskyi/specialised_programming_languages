# task №1
print("task №1")

number_1 = int(input("Введіть число №1: "))
number_2 = int(input("Введіть число №2: "))
operator = str(input("Введіть оператор (наприклад: +, -, *, /): "))

print(number_1, number_2, operator)

# task №2
print("task №2")


def task_2(operator):
    lst = ['+', '-', '*', '/']

    while True:
        if operator in lst:
            print("correct")
            break
        else:
            print("Помилка при введені оператора, введіть ще раз")
            operator = str(input("Введіть оператор (наприклад: +, -, *, /): "))


task_2(operator)

# task №3
print("task №3")

result = eval(f"{number_1} {operator} {number_2}")

print(f"Обчислення: {number_1} {operator} {number_2} = {result}")

# task №4
print("task №4")

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))

    if check == 'так':
        number_1 = int(input("Введіть число №1: "))
        number_2 = int(input("Введіть число №2: "))
        operator = str(input("Введіть оператор (наприклад: +, -, *, /): "))

        result = eval(f"{number_1} {operator} {number_2}")
        print(f"Обчислення: {number_1} {operator} {number_2} = {result}")
    elif check == 'ні':
        break
    else:
        print("Помилка введення, повторіть дію")

# task №5
print("task №5")

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))

    if check == 'так':
        try:

            number_1 = int(input("Введіть число №1: "))
            number_2 = int(input("Введіть число №2: "))
            operator = str(input("Введіть оператор (наприклад: +, -, *, /): "))
            task_2(operator)

        except ValueError:
            print("Помилка вводу одного з чисел")
            continue

        try:
            result = eval(f"{number_1} {operator} {number_2}")
        except ZeroDivisionError:
            print("Ділення на нуль неможливо")
            continue
        except SyntaxError:
            print("Помилка арифметичної операції")
            continue

        print(f"Обчислення: {number_1} {operator} {number_2} = {result}")
    elif check == 'ні':
        break
    else:
        print("Помилка введення, повторіть дію")


# task №6
print("task №6")

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))

    if check == 'так':
        try:

            number_1 = int(input("Введіть число №1: "))
            number_2 = int(input("Введіть число №2: "))
            operator = str(input("Введіть оператор (наприклад: +, -, *, /): "))
            task_2(operator)

        except ValueError:
            print("Помилка вводу одного з чисел")
            continue

        try:
            result = round(eval(f"{number_1} {operator} {number_2}"), 2)
        except ZeroDivisionError:
            print("Ділення на нуль неможливо")
            continue
        except SyntaxError:
            print("Помилка арифметичної операції")
            continue

        print(f"Обчислення: {number_1} {operator} {number_2} = {result}")
    elif check == 'ні':
        break
    else:
        print("Помилка введення, повторіть дію")


# task №7

print("task №7")

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))

    if check == 'так':
        try:

            number_1 = int(input("Введіть число №1: "))
            number_2 = int(input("Введіть число №2: "))
            operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                 "): "))

            lst = ['+', '-', '*', '/', '^', '√', '%']

            while True:
                if operator in lst:
                    break
                else:
                    print("Помилка при введені оператора, введіть ще раз")
                    operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                         "): "))
        except ValueError:
            print("Помилка вводу одного з чисел")
            continue

        try:
            if operator == '^':
                operator = '**'
            if operator != '√':
                result = round(eval(f"{number_1} {operator} {number_2}"), 2)
                message = f"Обчислення: {number_1} {operator} {number_2} = {result}"
            else:
                import math
                result = (round(math.sqrt(number_1), 2))
                message = f"Обчислення: {operator} {number_1}   = {result}"
        except ZeroDivisionError:
            print("Ділення на нуль неможливо")
            continue
        except SyntaxError:
            print("Помилка арифметичної операції")
            continue

        print(message)
    elif check == 'ні':
        break
    else:
        print("Помилка введення, повторіть дію")

# task №8

print("task №8")

history = []

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))

    if check == 'так':
        try:

            number_1 = int(input("Введіть число №1: "))
            number_2 = int(input("Введіть число №2: "))
            operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                 "): "))

            lst = ['+', '-', '*', '/', '^', '√', '%']

            while True:
                if operator in lst:
                    if operator == '^':
                        operator = '**'
                    break
                else:
                    print("Помилка при введені оператора, введіть ще раз")
                    operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                         "): "))
        except ValueError:
            print("Помилка вводу одного з чисел")
            continue

        try:
            if operator != '√':
                result = round(eval(f"{number_1} {operator} {number_2}"), 2)
                message = f"Обчислення: {number_1} {operator} {number_2} = {result}"
            else:
                import math
                result = (round(math.sqrt(number_1), 2))
                message = f"Обчислення: {operator} {number_1}   = {result}"
        except ZeroDivisionError:
            print("Ділення на нуль неможливо")
            continue
        except SyntaxError:
            print("Помилка арифметичної операції")
            continue

        print(message)

        save = input("Зберегти результат:(введіть так, якщо бажаєте) ")

        if save == 'так':
            history.append(result)
        else:
            continue

        output = input("Показати результати:(введіть так, якщо бажаєте) ")

        if output == 'так':
            print([result for result in history])
        else:
            continue
    elif check == 'ні':
        break
    else:
        print("Помилка введення, повторіть дію")
# task №9

print("task №9")

history = []

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))

    if check == 'так':
        try:

            number_1 = int(input("Введіть число №1: "))
            number_2 = int(input("Введіть число №2: "))
            operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                 "): "))

            lst = ['+', '-', '*', '/', '^', '√', '%']

            while True:
                if operator in lst:
                    if operator == '^':
                        operator = '**'
                    break
                else:
                    print("Помилка при введені оператора, введіть ще раз")
                    operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                         "): "))
        except ValueError:
            print("Помилка вводу одного з чисел")
            continue

        try:
            if operator != '√':
                result = round(eval(f"{number_1} {operator} {number_2}"), 2)
                message = f"Обчислення: {number_1} {operator} {number_2} = {result}"
            else:
                import math

                result = (round(math.sqrt(number_1), 2))
                message = f"Обчислення: {operator} {number_1}   = {result}"
        except ZeroDivisionError:
            print("Ділення на нуль неможливо")
            continue
        except SyntaxError:
            print("Помилка арифметичної операції")
            continue

        print(message)

        history.append(message)
        output = input("Показати історію:(введіть так, якщо бажаєте) ")

        if output == 'так':
            print([result for result in history])
        else:
            continue
    elif check == 'ні':
        break
    else:
        print("Помилка введення, повторіть дію")

# task №10

print("task №10")
history = []

while True:
    check = str(input("Виконати ще одне обчислення?(так/ні)"))
    if check == 'так':
        try:
            count = int(input("Введіть кількість знаків після коми: "))
            number_1 = int(input("Введіть число №1: "))
            number_2 = int(input("Введіть число №2: "))
            operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %" "): "))
            lst = ['+', '-', '*', '/', '^', '√', '%']
            while True:
                if operator in lst:
                    if operator == '^':
                        operator = '**'
                    break
                else:
                    print("Помилка при введені оператора, введіть ще раз")
                    operator = str(input("Введіть оператор (наприклад: +, -, *, /, ^, √, %"
                                         "): "))
        except ValueError:
            print("Помилка вводу одного з чисел")
            continue
        try:
            if operator != '√':
                result = round(eval(f"{number_1} {operator} {number_2}"), count)
                message = f"Обчислення: {number_1} {operator} {number_2} = {result}"
            else:
                import math
                result = (round(math.sqrt(number_1), 2))
                message = f"Обчислення: {operator} {number_1}   = {result}"
        except ZeroDivisionError:
            print("Ділення на нуль неможливо")
            continue
        except SyntaxError:
            print("Помилка арифметичної операції")
            continue
        print(message)
        history.append(message)
        output = input("Показати історію:(введіть так, якщо бажаєте) ")
        if output == 'так':
            print([result for result in history])
        else:
            continue
    else:
        break
        