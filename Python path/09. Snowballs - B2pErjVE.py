snowballs = int(input())

max_result = 0
max_weight = 0
max_time = 0
max_quality = 0


for i in range(snowballs):
    temp_result = 0
    weight = int(input())
    time = int(input())
    quality = int(input())

    temp_result = (weight / time) ** quality

    if temp_result > max_result:
        max_result = temp_result
        max_weight = weight
        max_time = time
        max_quality = quality

print(f'{max_weight} : {max_time} = {int(max_result)} ({max_quality})')
