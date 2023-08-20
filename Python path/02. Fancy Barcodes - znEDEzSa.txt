import re

num = int(input())

barcode = r'(@#{1,})([A-Z][A-Za-z0-9]{4,}[A-Z])(@#{1,})'
digits = r'\d'

for i in range(num):
    text = input()

    match_barcode = re.findall(barcode, text)

    if match_barcode:
        match_digits = re.findall(digits, text)

        if match_digits:
            print(f'Product group: {"".join(match_digits)}')
        else:
            print(f'Product group: 00')

    else:
        print(f'Invalid barcode')
