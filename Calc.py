print('Привет. Это калькулятор.')
result = "X"
repeat = "y"

while repeat == "y":
    num_1 = int(input ('Введи первое число:'))
    action = input ('Введи действие (или help для справки):')
    if action == "help":
        fr = open("Docs/Math_help.txt", "r", encoding="utf8")
        help = fr.read()
        fr.close()
        print (help)
        action = input('Введи действие:')
    num_2 = int(input ('Введи второе число:'))

    try:
        if action == "+":
            result = num_1 + num_2
        elif action == "-":
            result = num_1 - num_2
        elif action == "*":
            result = num_1 * num_2
        elif action == "/":
            result = num_1 / num_2
        elif action == "**":
            result = num_1 ** num_2
        elif action == "//":
            result = int(num_1 ** (1/num_2))
        else:
            print ('Нет такого действия')
    except ZeroDivisionError:
        print ("На 0 делить нельзя!")
    print("Ответ:", result)
    repeat = input("Новый расчет? (y/n):")
    if repeat == "y":
        continue
    else:
        print("Спасибо. До свидания")
        break

