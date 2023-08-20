number_of_students = int(input())

d = {}

for i in range(number_of_students):
    data = input().split()
    name = data[0]
    grade = float(data[1])

    if name not in d:
        d[name] = []

    d[name].append("%.2f" % grade)


[print(f'{key} -> {" ".join(map(str,value))} (avg: {sum(map(float,value)) / len(value):.2f})') for key, value in d.items()]

