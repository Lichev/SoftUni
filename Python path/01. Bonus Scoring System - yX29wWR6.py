import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
student = 0

for x in range(number_of_students):
    attendance = int(input())
    total_bonus = (attendance/ number_of_lectures) * (5 + additional_bonus)

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        student = attendance

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {student} lectures.")