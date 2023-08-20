budget = float(input())
videokarti = int(input())
procesori = int(input())
ram = int(input())

cenaVideo = videokarti * 250
cenaPro = procesori * (cenaVideo * 0.35)
cenaRam = ram * (cenaVideo * 0.10)
kraina = cenaVideo + cenaPro + cenaRam

if videokarti > procesori:
    kraina = kraina - (kraina * 0.15)

razlika1 = budget - kraina
razlika2 = kraina - budget

if budget >= kraina:
    print(f'You have {razlika1:.2f} leva left!')
else:
    print(f'Not enough money! You need {razlika2:.2f} leva more!')