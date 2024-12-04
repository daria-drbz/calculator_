def calc(input_line):
    """
    Функция принимает строку с текстовым представлением чисел и операций,
    возвращает результат выражения в виде текста.
    """
    #убираем лишние пробелы
    input_line = input_line.strip()

    # создаем словарь
    words_to_symbols = {
        "один": "1", "два": "2", "три": "3", "четыре": "4", "пять": "5", "шесть": "6",
        "семь": "7", "восемь": "8", "девять": "9", "десять": "10", "одиннадцать": "11",
        "двенадцать": "12", "тринадцать": "13", "четырнадцать": "14", "пятнадцать": "15",
        "шестнадцать": "16", "семнадцать": "17", "восемнадцать": "18", "девятнадцать": "19",
        "двадцать": "20", "тридцать": "30", "сорок": "40", "пятьдесят": "50",
        "шестьдесят": "60", "семьдесят": "70", "восемьдесят": "80", "девяносто": "90",
        "плюс": "+", "минус": "-", "умножить": "*", "на": "",
        "открывается": "(", "закрывается": ")", "скобка": "",
        "ноль": "0"
    }

    # список слов из строки
    words = input_line.split()
    expression = ""

    # построение математического выражения
    for word in words:
        if word in words_to_symbols:
            expression += words_to_symbols[word]
        else:
            return "Ошибка: Некорректное слово в вводе"

    # проверка баланса скобок
    if expression.count("(") != expression.count(")"):
        return "Ошибка: Несбалансированные скобки"

    try:
        # вычисление результата
        numeric_result = eval(expression)
    except Exception:
        return "Ошибка: Некорректное математическое выражение"

    # словарь для преобразования чисел обратно в текст
    numbers_to_words = {v: k for k, v in words_to_symbols.items()}
    result_str = str(numeric_result)

    # преобразование числового результата в текст
    if numeric_result < 0:
        result_words = "минус "
        result_str = result_str[1:]  # Убираем минус
    else:
        result_words = ""

    if result_str in numbers_to_words:
        return result_words + numbers_to_words[result_str]

    # обработка сложных чисел
    for index, digit in enumerate(result_str):
        if digit != "0":
            factor = len(result_str) - index - 1
            result_words += numbers_to_words[digit + "0" * factor] + " "

    return result_words.strip()


# пример вызова функции
expression = input("Введите строковое выражение для вычисления: ")
print(calc(expression))