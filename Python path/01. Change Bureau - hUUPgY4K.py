number_of_bitcoins = int(input())
number_of_uan = float(input())
comission = float(input())


btc_to_lv = number_of_bitcoins * 1168
uan_to_dlr = number_of_uan * 0.15
dlr_to_lv = uan_to_dlr * 1.76
all_lv = btc_to_lv + dlr_to_lv
lv_to_euro = all_lv / 1.95
com = lv_to_euro * (comission / 100)
all = lv_to_euro - com

print(f'{all:.2f}')