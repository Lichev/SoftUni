visitors = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0
workout = 0
buy = 0


for i in range(visitors):
    workout_type = input()

    if workout_type == 'Back':
        back += 1
        workout += 1
    elif workout_type == 'Chest':
        chest += 1
        workout += 1
    elif workout_type == 'Legs':
        legs += 1
        workout += 1
    elif workout_type == 'Abs':
        abs += 1
        workout += 1
    elif workout_type == 'Protein shake':
        protein_shake += 1
        buy += 1
    elif workout_type == 'Protein bar':
        protein_bar += 1
        buy += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(workout / visitors) * 100:.2f}% - work out")
print(f"{(buy / visitors) * 100:.2f}% - protein")