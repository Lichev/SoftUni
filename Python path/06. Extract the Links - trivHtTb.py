import re

text = input()


while text != '':
    example = r'((www).([A-Za-z0-9\-]+)(\.[A-Za-z]+)(\.?[A-Za-z0-9\-]*)*)'
    matching = re.search(example, text)

    if matching:
        printer = matching.group(1)

        print(printer)


    text = input()