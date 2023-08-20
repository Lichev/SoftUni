def even_odd(*args):
    command = args[-1]

    def even():
        even_lst = []
        for x in range(len(args) - 1):
            if args[x] % 2 == 0:
                even_lst.append(args[x])
        return even_lst
    def odd():
        odd_list = []
        for x in range(len(args) - 1):
            if args[x] % 2 != 0:
                odd_list.append(args[x])
        return odd_list

    if command == 'even':
        return even()
    else:
        return odd()


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))