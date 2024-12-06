def number_to_words(n):
    """Преобразует число в диапазоне [-100, 100] в текстовое представление."""
    words_to_numbers = {
        1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть",
        7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать",
        12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
        16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать",
        20: "двадцать", 30: "тридцать", 40: "сорок", 50: "пятьдесят",
        60: "шестьдесят", 70: "семьдесят", 80: "восемьдесят", 90: "девяносто",
        100: "сто"
    }

    if -100 <= n <= 100:
        if n < 0:
            return "минус " + number_to_words(abs(n))
        elif n in words_to_numbers:
            return words_to_numbers[n]
        elif 20 < n < 100:
            tens = n // 10 * 10
            units = n % 10
            return words_to_numbers[tens] + ((" " + words_to_numbers[units]) if units else "")
        # Для чисел вне диапазона [-100, 100]
    return str(n)


def calc(input_line):
    input_line = input_line.strip()

    words_to_symbols = {
        "один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6,
        "семь": 7, "восемь": 8, "девять": 9, "десять": 10, "одиннадцать": 11,
        "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
        "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19,
        "двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50,
        "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80, "девяносто": 90,
        "сто": 100,
        "плюс": "+", "минус": "-", "умножить": "*", "на": "*",
        "делить": "/",
        "открытая": "(", "закрытая": ")",
    }

    words = input_line.split()
    expression = ""
    current_number = None

    for word in words:
        if word in words_to_symbols:
            if isinstance(words_to_symbols[word], int):
                if current_number is None:
                    current_number = words_to_symbols[word]
                else:
                    current_number += words_to_symbols[word]
            else:
                if current_number is not None:
                    expression += str(current_number)
                    current_number = None
                expression += words_to_symbols[word]
        else:
            return f"Ошибка: Некорректное слово '{word}' в вводе"

    if current_number is not None:
        expression += str(current_number)

    if expression.count("(") != expression.count(")"):
        return "Ошибка: Несбалансированные скобки"

    try:
        numeric_result = eval(expression) 
    except (TypeError, ValueError, ZeroDivisionError, SyntaxError, NameError) as e:
        return f"Ошибка вычисления: {e}"

    result_str = number_to_words(numeric_result)
    return result_str


# пример вызова функции
expression = input("Введите строковое выражение для вычисления: ")
print(calc(expression))
