number_of_tabs = int(input())
salary = int(input())

penalty = 0

for i in range (number_of_tabs):
    name_of_site = input()

    if name_of_site == 'Facebook':
        penalty += 150
    elif name_of_site == 'Instagram':
        penalty += 100
    elif name_of_site == 'Reddit':
        penalty += 50


diff = abs(salary - penalty)

if salary <= penalty:
    print(f'You have lost your salary.')
else:
    print(int(diff))