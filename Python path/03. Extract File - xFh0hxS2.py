path_name = input().split("\\")
file = path_name[-1]
files = file.split(".")
first = files[0]
second = files[1]

print(f'File name: {first}')
print(f'File extension: {second}')