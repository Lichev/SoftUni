number = input()

new = []

for i in range(len(number)):
    new.append(number[i])

result = list(map(int, new))
print(*sorted(result, key=int, reverse=True), sep='')
