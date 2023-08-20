import math
recordSec = float(input())
metri = float(input())
sec = float(input())

forSwim = metri * sec
zabavqne = math.floor(metri / 15)
zabavqneSek = zabavqne * 12.5

obshto = forSwim + zabavqneSek

razlika = obshto - recordSec

if recordSec <= obshto:
    print(f'No, he failed! He was {razlika:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {obshto:.2f} seconds.')