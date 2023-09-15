import time


def inputNumber() -> int:
    try:
        return int(input("Введите число: "))
    except:
        raise


def inputFileName() -> str:
    return input("Введите имя файла для импорта: ")


def getInputBody() -> str:
    print("Для того, чтобы завершить запить, в новой строке введите \'Exit\' \n")
    data = "Boby: "
    while True:
        temp = input()
        if temp == "Exit":
            return data
        else:
            data += '\n' + temp


def getInputTitle() -> str:
    return "Title: " + input("Введите имя записки! ")


def inputDate() -> str:
    print("Пожалуйста введите дату в формате дд.мм.гггг")
    while True:
        inputdata = input()
        try:
            return time.strptime(inputdata, "%d.%m.%Y")
        except Exception:
            print("Введены некорректные данные!")