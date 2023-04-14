def a1():
    try:
        number = int(input("Введите число: "))
    except ValueError:
        print("Было введено не число")
    else:
        if number % 2 == 0:
            print(f"{number} делится на 2")
        elif number == 0:
            print("Введен 0")
        else:
            print(f"{number} не делится на 2")

def a2():
    try:
        n = int(input("Введите число: "))
        v = 100 / n
    except ValueError:
        print("Введено не число!")
    except ZeroDivisionError:
        print("Введен 0!")
    else:
        print(f"100 : {n} = {v}")

def a3():
    d = input("Введите дату: ")
    d = d.split(".")
    if int(d[0]) * int(d[1]) == int(d[2][2 : 4]):
        print("Дата подходит")
    else:
        print("Дата не подходит")

def a4():
    ch = input("Введите номер из смс: ")
    x = 0
    y = 0
    if len(ch) % 2 == 0:
        for i in ch[0:int(len(ch) / 2)]:
            x = x + int(i)
        for i in ch[int(len(ch) / 2):int(len(ch)) + 1]:
            y = y + int(i)
        if x == y:
            print("вы выиграли автомобиль")
        else:
            print("вам не повезло")
    else:
        print("вы ввели не тот номер")