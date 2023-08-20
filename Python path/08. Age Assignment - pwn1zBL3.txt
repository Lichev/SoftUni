def age_assignment(*args, **kwargs):
    new_dict = {}
    lst = []
    for x in args:
        first_letter = x[0]
        age = 0
        if x[0] in kwargs:
            age = kwargs[first_letter]
            new_dict[x] = age
    new_dict = sorted(new_dict.items(), key=lambda x: x[0])
    new_dict = dict(new_dict)

    for name, age in new_dict.items():
        lst.append(f"{name} is {age} years old.")

    return "\n".join(lst)


print(age_assignment("Peter", "George", G=26, P=19))
print()
print(age_assignment("Amy", "Bill", "Willy", W=36,A=22, B=61))