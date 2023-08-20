text = input().split(', ')


if text[-1] == 'wolf':
    print(f'Please go away and stop eating my sheep')
else:
    text.reverse()
    index = text.index('wolf')
    print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')