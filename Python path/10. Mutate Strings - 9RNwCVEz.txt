one = input()
two = input()

for i in range(len(two)):
    if one[i] != two[i]:
        replacement = two[i]

        word = one[0:i] + replacement + one[i + 1:]
        one = word
        print(one)
