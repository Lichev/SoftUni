import math

name_of_show = input()
time_of_episode = int(input())
time_of_break = int(input())

obqd = time_of_break * 0.125
otdih = time_of_break * 0.25
ostanalo = time_of_break - obqd - otdih

razlika1 = time_of_episode - ostanalo
razlika2 = ostanalo - time_of_episode

if time_of_episode <= ostanalo:
    print(f'You have enough time to watch {name_of_show} and left with {math.ceil(razlika2)} minutes free time.')
else:
    print(f'You dont have enough time to watch {name_of_show}, you need {math.ceil(razlika1)} more minutes.')