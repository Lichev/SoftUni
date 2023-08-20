import re

n = int(input())

decription_key = r'[s,t,a,r,S,T,A,R]'
info = r'@(?P<planet>[A-Za-z]+)([^\@\-\!\:\>]+)?:(?P<population>[0-9]+)([^\@\-\!\:\>]+)?!(?P<type>[A|D])!([^\@\-\!\:\>]+)?->(?P<soldiers>[0-9]+)'

attacked_planets = []
destroyed_planets = []

for i in range(n):
    text = input()

    find_key = re.findall(decription_key, text)
    key = len(find_key)

    decrypted_text = ''
    for w in text:
        before = ord(w) - key
        decrypted_text += chr(before)

    planets_info = re.finditer(info, decrypted_text)

    for match in planets_info:
        planet = match.group('planet')
        population = match.group('population')
        attack = match.group('type')
        soldiers = match.group('soldiers')

        if attack == 'A':
            attacked_planets.append(planet)
        else:
            destroyed_planets.append(planet)

print(f'Attacked planets: {len(attacked_planets)}')
if len(attacked_planets) > 0:
    [print(f'-> {i}') for i in sorted(attacked_planets)]
print(f'Destroyed planets: {len(destroyed_planets)}')
if len(destroyed_planets) > 0:
    [print(f'-> {x}') for x in sorted(destroyed_planets)]