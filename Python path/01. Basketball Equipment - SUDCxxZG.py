tax = float(input())

shoes = tax - (tax * 0.40)
ekip = shoes - (shoes * 0.20)
ball = ekip * 0.25
accesor = ball * 0.2
all = shoes + ekip + ball + accesor + tax

print(f'{all:.2f}')

