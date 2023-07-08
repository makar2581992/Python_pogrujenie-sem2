# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


def convert_number(num: int, mode: str) -> str:
    result = ''
    convert: int = 2
    match mode:
        case "hex":
            convert = 16
    while num >= 1:
        res = num % convert
        if convert == 16:
            if res == 10:
                res = 'A'
            if res == 11:
                res = 'B'
            if res == 12:
                res = 'C'
            if res == 13:
                res = 'D'
            if res == 14:
                res = 'E'
            if res == 15:
                res = 'F'
        result += str(res)
        num = num // convert
    return result[::-1]

number = int(input("Введите число: "))
print(convert_number(number, mode="hex"),
    f"\nПроверка методом hex: {hex(number)}")