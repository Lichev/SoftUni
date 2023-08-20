numbers = [int(x) for x in input().split(', ')]

positive = [p for p in numbers if p >= 0]
negative = [n for n in numbers if n < 0]
even = [e for e in numbers if e % 2 == 0]
odd = [o for o in numbers if o % 2 != 0]

print(f'Positive:', ', '.join(map(str, positive)))
print(f'Negative:', ', '.join(map(str, negative)))
print(f'Even:', ', '.join(map(str, even)))
print(f'Odd:', ', '.join(map(str, odd)))
