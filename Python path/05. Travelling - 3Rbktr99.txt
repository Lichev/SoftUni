while True:
    destination = input()
    if destination == 'End':
        break
    budget = float(input())
    count = 0
    while count < budget:
        money = float(input())
        count += money

    if count >= budget:
        print(f'Going to {destination}!')
