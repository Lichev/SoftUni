strawberry_price = float(input())
bananas_quantity = float(input())
portocal_quantity = float(input())
malini_quantity = float(input())
strawberry_quantity = float(input())

qgodi = strawberry_quantity * strawberry_price
malini_cena = strawberry_price / 2
malini = malini_quantity * malini_cena
portokali = portocal_quantity * (malini_cena - (malini_cena * 0.40))
banani = bananas_quantity * (malini_cena - (malini_cena * 0.80))
sum= qgodi + malini + portokali + banani

print(f'{sum:.2f}')