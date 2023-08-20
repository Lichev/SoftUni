import os
import csv


def take_lines_for_factor(price_exception_path):
    storage_add_factor = []
    for_duplicate = []
    with open(price_exception_path, 'r', encoding='UTF8') as file:
        content = csv.reader(file, delimiter='\t')
        key_add = 'add'
        for line in content:
            if key_add in line[15]:
                key_duplicate = f'{line[2]} - {line[3]} - {line[4]}'
                PRICELB = float(line[12]) * 0.6
                PRICEUB = float(line[12]) * 1.3
                crefsuffix = line[4] if line[4] else ''
                current = [line[2], line[3], '', crefsuffix, f'{PRICELB:.2f}', f'{PRICEUB:.2f}', '', '', '', line[16],
                           line[10]]
                if line not in storage_add_factor and key_duplicate not in for_duplicate:
                    storage_add_factor.append(current)
                    for_duplicate.append(key_duplicate)

    return storage_add_factor


def take_lines_already_with_factor(price_exception_path):
    storage_already_factor = []
    for_duplicate = []
    with open(price_exception_path, 'r', encoding='UTF8') as file:
        content = csv.reader(file, delimiter='\t')
        key_add = 'add'
        for line in content:
            if key_add in line[15]:
                key_duplicate = f'{line[18]} - {line[3]}'
                if line[2] == line[18]:
                    current = [line[18], line[3], line[19], line[23], line[24], line[20], line[21], line[12]]
                    if line not in storage_already_factor and key_duplicate not in for_duplicate:
                        storage_already_factor.append(current)
                        for_duplicate.append(key_duplicate)

    return storage_already_factor


def merge_already_applied_with_not_applied(add_factor, already_factor):
    final_for_adding = []
    for add in add_factor:
        for already in already_factor:
            if already[0] == add[0] and already[1] == add[1]:
                add[6] = already[3]
                add[7] = already[4]
                add[2] = already[2].strip()
                add[4] = already[5]
                add[5] = already[6]

                if float(already[7]) < float(already[5]):
                    add[4] = f'{float(already[7]) * 0.6:.2f}'
                elif float(already[7]) > float(already[6]):
                    add[5] = f"{float(already[7]) * 1.2:.2f}"
        final_for_adding.append(add)
    return final_for_adding


def take_bsh_for_min_period(bsh_path, after_merge):
    lst = []
    for line in after_merge:
        with open(bsh_path, 'r', encoding='UTF8') as file:
            content = csv.reader(file, delimiter='\t')
            min_period = 9999
            for bsh in content:
                if line[0] == bsh[8] and line[1] == bsh[4]:
                    if float(line[4]) <= float(bsh[11]) <= float(line[5]):
                        if min_period > int(bsh[0]):
                            min_period = int(bsh[0])
            lst.append([line[0], line[1], min_period])

    return lst


def take_min_period_from_bsh(after_merge_for_add, period_from_bsh):
    lst = []

    for add in after_merge_for_add:
        for bsh in period_from_bsh:
            if add[0] == bsh[0] and add[1] == bsh[1] and len(add[6]) == 0:
                add[6] = bsh[2]
                add[7] = 9999
        lst.append(add)
    return lst


# with open('add_factor.txt', 'w', encoding='UTF8', newline='') as new_f:
#     # Write the lines from store_lines list
#     writer = csv.writer(new_f, delimiter='\t')
#     for_print = set(storage_add_factor)
#     for line in for_print:
#         writer.writerow(line)


if __name__ == '__main__':
    price_exception_path = 
    bsh_path = 

    # Here we take all the lines for factor from PE report
    add_factor = take_lines_for_factor(price_exception_path)

    # Here we take which already factor and we have to change and delete it first
    already_factor = take_lines_already_with_factor(price_exception_path)

    # Here we add the same periods from already existing factors
    after_merge_for_add = merge_already_applied_with_not_applied(add_factor, already_factor)

    # Here we take the min period from bsh and add them to the list for add factor
    periods_from_bsh = take_bsh_for_min_period(bsh_path, after_merge_for_add)

    final_list = take_min_period_from_bsh(after_merge_for_add, periods_from_bsh)



    # # [print('\t'.join(map(str, x))) for x in add_factor]
    # # print(len(add_factor))
    # # print()
    #
    # [print('\t'.join(map(str, x))) for x in already_factor]
    # print(len(already_factor))
    # print()
    # #
    # [print('\t'.join(map(str, x))) for x in after_merge_for_add]
    # print(len(after_merge_for_add))
    # print()

    [print('\t'.join(map(str, x))) for x in periods_from_bsh]
    print(len(periods_from_bsh))
    print()

    [print('\t'.join(map(str, x))) for x in final_list]
    print(len(final_list))
    print()


