leader = ''
score = 0

while True:
    player_name = input()

    if player_name == 'END':
        break
    goals: int = int(input())

    if goals > score:
        leader = player_name
        score = goals
    if goals >= 10:
        break

if score >= 3:
    print(f"{leader} is the best player!")
    print(f"He has scored {score} goals and made a hat-trick !!!")
else:
    print(f"{leader} is the best player!")
    print(f"He has scored {score} goals.")