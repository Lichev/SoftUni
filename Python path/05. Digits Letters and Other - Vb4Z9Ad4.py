word = input()

digits = [chr for chr in word if chr.isdigit()]
letter = [x for x in word if x.isalpha()]
rest = [i for i in word if i not in digits and i not in letter]


print("".join(digits))
print("".join(letter))
print("".join(rest))
