key = int(input())
lines = int(input())

chars = []

for i in range(lines):
    code = input()
    crack = ord(code) + key

    chars.append(chr(crack))

print(''.join(chars))