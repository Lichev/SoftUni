def cast_spell(heroes_of_code, hero, mp, spell):
    if heroes_of_code[hero]['MP'] >= mp:
        heroes_of_code[hero]['MP'] -= mp
        print(f"{hero} has successfully cast {spell} and now has {heroes_of_code[hero]['MP']} MP!")
    else:
        print(f"{hero} does not have enough MP to cast {spell}!")

    return heroes_of_code


def take_damage(heroes_of_code, hero, damage, attacker):
    heroes_of_code[hero]['HP'] -= damage

    if heroes_of_code[hero]['HP'] > 0:
        print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes_of_code[hero]['HP']} HP left!")
    else:
        print(f"{hero} has been killed by {attacker}!")
        del heroes_of_code[hero]

    return heroes_of_code


def recharge(heroes_of_code, hero, mp):
    needed_mp = 200 - heroes_of_code[hero]['MP']
    if heroes_of_code[hero]['MP'] + mp > 200:
        heroes_of_code[hero]['MP'] = 200
        print(f"{hero} recharged for {needed_mp} MP!")
    else:
        heroes_of_code[hero]['MP'] += mp
        print(f"{hero} recharged for {mp} MP!")

    return heroes_of_code


def heal(heroes_of_code, hero, hp):
    needed_hp = 100 - heroes_of_code[hero]['HP']
    if heroes_of_code[hero]['HP'] + hp > 100:
        heroes_of_code[hero]['HP'] = 100
        print(f"{hero} healed for {needed_hp} HP!")
    else:
        heroes_of_code[hero]['HP'] += hp
        print(f"{hero} healed for {hp} HP!")

    return heroes_of_code


n = int(input())
heroes_of_code = {}

for n in range(n):
    info = input().split(' ')
    hero_name = info[0]
    HP = int(info[1])
    MP = int(info[2])

    heroes_of_code[hero_name] = {}
    heroes_of_code[hero_name]['HP'] = HP
    heroes_of_code[hero_name]['MP'] = MP

command = input()

while command != 'End':
    command = command.split(' - ')
    action = command[0]

    if action == 'CastSpell':
        cast_hero = command[1]
        cast_mp = int(command[2])
        spell_name = command[3]
        heroes_of_code = cast_spell(heroes_of_code, cast_hero, cast_mp, spell_name)

    elif action == 'TakeDamage':
        damage_her = command[1]
        damage = int(command[2])
        attacker = command[3]

        heroes_of_code = take_damage(heroes_of_code, damage_her, damage, attacker)

    elif action == 'Recharge':
        recharge_her = command[1]
        amount_mp = int(command[2])
        heroes_of_code = recharge(heroes_of_code, recharge_her, amount_mp)

    elif action == 'Heal':
        heal_her = command[1]
        amount_hp = int(command[2])
        heroes_of_code = heal(heroes_of_code, heal_her, amount_hp)

    command = input()

for primary in heroes_of_code.keys():
    print(primary)
    [print(f' {key}: {value}') for key, value in heroes_of_code[primary].items()]
