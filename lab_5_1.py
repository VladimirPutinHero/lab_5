def longest_common_prefix(words):
    if not words:
        return ''

    shortest_word = min(words, key=len)
    for i, char in enumerate(shortest_word):
        for other_word in words:
            if other_word[i] != char:
                return shortest_word[:i]

    return shortest_word


if __name__ == '__main__':
    words = []
    while True:
        word = input("Введите слово (или 'стоп' для выхода): ")
        if word.lower() == 'стоп':
            break
        if not word.isalpha():
            print("Введите только буквы!")
            continue
        words.append(word)

    result = longest_common_prefix(words)
    print(f"Наибольший общий префикс: {result}")
