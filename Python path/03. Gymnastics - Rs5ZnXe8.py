country = input()
ured = input()


result = 0
difficulty = 0
execution = 0


if country == 'Russia':
    if ured == 'ribbon':
        difficulty = 9.100
        execution = 9.400
        result = difficulty + execution
    elif ured == 'hoop':
        difficulty = 9.300
        execution = 9.800
        result = difficulty + execution
    elif ured == 'rope':
        difficulty = 9.600
        execution = 9.000
        result = difficulty + execution

elif country == 'Bulgaria':
    if ured == 'ribbon':
        difficulty = 9.600
        execution = 9.400
        result = difficulty + execution
    elif ured == 'hoop':
        difficulty = 9.550
        execution = 9.750
        result = difficulty + execution
    elif ured == 'rope':
        difficulty = 9.500
        execution = 9.400
        result = difficulty + execution

elif country == 'Italy':
    if ured == 'ribbon':
        difficulty = 9.200
        execution = 9.500
        result = difficulty + execution
    elif ured == 'hoop':
        difficulty = 9.450
        execution = 9.350
        result = difficulty + execution
    elif ured == 'rope':
        difficulty = 9.700
        execution = 9.150
        result = difficulty + execution

points = 20
forthewin = points - result
percent = (forthewin / 20) * 100

print(f'The team of {country} get {result:.3f} on {ured}.')
print(f'{percent:.2f}%')