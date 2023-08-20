minutes = int(input())
seconds = int(input())
lenght = float(input())
sec_for_100 = int(input())

min_to_sec = (minutes * 60) + seconds
time_to_decrease = lenght / 120
obshto = time_to_decrease * 2.5

marin_time = (lenght / 100) * sec_for_100 - obshto

diff = abs(min_to_sec - marin_time)
if marin_time <= min_to_sec:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time:.3f}.')
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
