def start_spring(**kwargs):
    dct = {}

    for key, value in kwargs.items():
        if value not in dct:
            dct[value] = []

        dct[value].append(key)

    dct = dict(sorted(dct.items(), key=lambda x: (-len(x[1]), x[0],)))

    lst = []
    for key, value in dct.items():
        lst.append(key + ':')
        dct[key] = sorted(value, key= lambda x: x)
        for v in dct[key]:
            lst.append("-" + v)


    return '\n'.join(lst)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

print()

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

print()

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))