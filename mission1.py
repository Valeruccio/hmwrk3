print("Задание 1")


def div(*args):

    try:
        arg1 = int(input("Введите делимое: "))
        arg2 = int(input("Введите делитель: "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "Неправильный делитель, на ноль делить нельзя!"

    return res

print(f'result  {div()}')