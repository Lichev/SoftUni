def words_sorting(*args):
    d = {}
    total = 0
    for x in args:
        values = sum([ord(s) for s in x])
        total += values

        d[x] = values

    if total % 2 != 0:
        final = dict(sorted(d.items(), key=lambda x: -x[1]))
    else:
        final = dict(sorted(d.items(), key=lambda x: x[0]))

    lst = []
    for k, v in final.items():
        lst.append(k + ' - ' + str(v))

    return '\n'.join(lst)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print()

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print()

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))