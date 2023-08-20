player_one = int(input())
player_two = int(input())

one_score = player_one
two_score = player_two


while one_score > 0 and two_score > 0:
    command = input()

    if command == 'End of battle':
        break

    if command == 'one':
        two_score -= 1
    elif command == 'two':
        one_score -= 1


if one_score == 0:
    print(f"Player one is out of eggs. Player two has {two_score} eggs left.")
elif two_score == 0:
    print(f"Player two is out of eggs. Player one has {one_score} eggs left.")
else:
    print(f"Player one has {one_score} eggs left.")
    print(f"Player two has {two_score} eggs left.")

