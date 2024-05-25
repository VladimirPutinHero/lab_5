def roman_to_arabic(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10,
                      'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    arabic_number = 0
    prev_value = 0

    for char in s:
        if char not in roman_numerals:
            return "ошибка"

        current_value = roman_numerals[char]
        if prev_value < current_value:
            arabic_number += current_value - 2 * prev_value
        else:
            arabic_number += current_value
        prev_value = current_value

    return arabic_number


if __name__ == '__main__':
    n = input('Введите римскую цифру (число): ')
    print(roman_to_arabic(n))
