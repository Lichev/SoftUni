number = [int(num) for num in input().split()]


lent = int(len(number) / 2 )
lists = list()
first_half = number[:lent]
second_half = number[lent + 1:]

left_score = 0
right_score = 0

for i in first_half:

    if i > 0:
        left_score += i
    else:
        left_score = left_score * 0.8

for n in second_half[::-1]:
    if n > 0:
        right_score += n
    else:
        right_score = right_score * 0.8


if left_score < right_score:
    print(f"The winner is left with total time: {left_score:.1f}")
else:
    print(f"The winner is right with total time: {right_score:.1f}")