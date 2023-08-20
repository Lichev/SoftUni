type_of_project = input()
line = int(input())
column = int(input())

seats = line * column
results = 0

if type_of_project == 'Premiere':
    results = seats * 12.00
elif type_of_project == "Normal":
    results = seats * 7.50
elif type_of_project == "Discount":
    results = seats * 5.00


print(f"{results:.2f} leva")