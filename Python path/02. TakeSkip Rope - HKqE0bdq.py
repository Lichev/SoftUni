def list_of_digits(numbers):
    digits = [x for x in numbers if x.isdigit()]
    return digits


def list_of_rest(non_numbers):
    rest = [i for i in non_numbers if not i.isdigit()]
    return rest


def general(text):
    list_digits = list(map(int, list_of_digits(text)))
    list_rest = list_of_rest(text)
    word = "".join(list_rest)
    take_word = []

    start = 0
    end = 0
    for index, i in enumerate(list_digits):
        end = start + i
        if end > len(word):
            end = len(word)

        if index % 2 == 0:
            for x in range(start, end):
                take_word.append(word[x])
                start += 1
        else:
            for x in range(start, end):
                start += 1
                continue

    print(*take_word, sep='')


words = input()
general(words)
