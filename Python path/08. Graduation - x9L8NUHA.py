name = input()

grade = 0
skusan = 0
averege = 0
bad_grade_condition = False
while grade < 12:
    score = float(input())
    if score < 4:
        skusan += 1
        if skusan > 1:
            bad_grade_condition = True
            grade += 1
            break
    else:
        averege += score
        grade += 1

if bad_grade_condition:
    print(f'{name} has been excluded at {grade} grade')
else:
    averege /= grade
    print(f'{name} graduated. Average grade: {averege:.2f}')
