name = input()
number_of_tickets = int(input())
kids_tickets = int(input())
neto = float(input())
obslujvane = float(input())


cena_kid = (neto - (neto * 0.70)) + obslujvane
cena_old = neto + obslujvane

all = (kids_tickets * cena_kid) + (number_of_tickets * cena_old)
after = all * 0.20


print(f"The profit of your agency from {name} tickets is {after:.2f} lv.")
