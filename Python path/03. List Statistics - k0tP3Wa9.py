n = int(input())

positives = list()
negatives = list()

for i in range(n):
    numbers = int(input())

    if numbers >= 0:
        positives.append(numbers)
    else:
        negatives.append(numbers)

print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')