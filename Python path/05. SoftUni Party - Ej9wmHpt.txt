n = int(input())

vip = set()
normal = set()


for i in range(n):
    guest_number = input()

    if guest_number[0].isdigit():
        vip.add(guest_number)
    else:
        normal.add(guest_number)

while True:
    command = input()

    if command == 'END':
        break

    if command[0].isdigit():
        vip.remove(command)
    else:
        normal.remove(command)

print(len(vip) + len(normal))
[print(s) for s in sorted(vip)]
[print(v) for v in sorted(normal)]
