hour_of_examp = int(input())
min_of_examp = int(input())
hour_of_arrive = int(input())
min_of_arrive = int(input())

minutesExamp = hour_of_examp * 60 + min_of_examp
minutesArrive = hour_of_arrive * 60 + min_of_arrive
diff = abs(minutesArrive - minutesExamp)

if minutesExamp == minutesArrive:
    print("On time")
elif minutesArrive > minutesExamp:
    print('Late')
    hours = diff // 60
    minutes = diff % 60

    if diff > 59:
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')

elif minutesArrive < minutesExamp:
    if diff > 30:
        print("Early")
    else:
        print('On time')
    hours = diff // 60
    minutes = diff % 60
    if diff > 59:
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{minutes} minutes before the start')