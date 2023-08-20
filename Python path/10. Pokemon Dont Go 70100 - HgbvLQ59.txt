sequence = [int(x) for x in input().split(" ")]

removed_elements = []

while len(sequence) != 0:
    indexes = int(input())

    if 0 <= indexes < len(sequence):
        for index, current_pokemon in enumerate(sequence):
            if sequence[indexes] >= current_pokemon and index != indexes:
                sequence[index] += sequence[indexes]
            elif sequence[indexes] < current_pokemon and index != indexes:
                sequence[index] -= sequence[indexes]
        removed_elements.append(sequence[indexes])
        sequence.remove(sequence[indexes])

    elif indexes >= len(sequence):
        removed_elements.append(sequence[-1])
        del sequence[-1]
        sequence.append(sequence[0])
        for index, current_pokemon in enumerate(sequence):
            if removed_elements[-1] >= current_pokemon:
                sequence[index] += removed_elements[-1]
            elif removed_elements[-1] < current_pokemon:
                sequence[index] -= removed_elements[-1]

    elif indexes < 0:
        removed_elements.append(sequence[0])
        del sequence[0]
        sequence.insert(0, sequence[-1])

print(sum(map(int, removed_elements)))