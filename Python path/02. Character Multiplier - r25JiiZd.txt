text = input().split(" ")
first = text[0]
second = text[1]
lenght1 = len(first)
lenght2 = len(second)
result = 0


if lenght1 > lenght2:
    for index in range(lenght2):
        result += ord(first[index]) * ord(second[index])
    for index in range(lenght2, lenght1):
        result += ord(first[index])

elif lenght2 > lenght1:
    for index in range(lenght1):
        result += ord(first[index]) * ord(second[index])
    for index in range(lenght1, lenght2):
        result += ord(second[index])
else:
    for i in range(0, lenght1):
        result += ord(first[i]) * ord(second[i])


print(result)