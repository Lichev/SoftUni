snowballs = int(input())

result = 0
weight = 0
time = 0
quality = 0

for i in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    calc = (snowball_weight / snowball_time) ** snowball_quality

    if calc > result:
        result = calc
        weight = snowball_weight
        time = snowball_time
        quality = snowball_quality

print(f"{weight} : {time} = {int(result)} ({quality})")