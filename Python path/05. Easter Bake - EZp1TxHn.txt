import math
import sys

number_of_kozunak = int(input())

all_sheker = 0
all_brashnu = 0

max_sheker = -sys.maxsize
max_brashnu = -sys.maxsize

for i in range(number_of_kozunak):
    sheker = int(input())
    brashnu = int(input())


    all_sheker += sheker
    all_brashnu += brashnu

    if sheker > max_sheker:
         max_sheker = sheker
    if brashnu > max_brashnu:
        max_brashnu = brashnu

result_sheker = all_sheker / 950
result_brasno = all_brashnu / 750


print(f'Sugar: {math.ceil(result_sheker)}')
print(f"Flour: {math.ceil(result_brasno)}")
print(f"Max used flour is {max_brashnu} grams, max used sugar is {max_sheker} grams.")