start = ord(input())
end = ord(input())
text = input()

total = 0
for char in text:
    num_of_char = ord(char)

    if start < num_of_char < end:
        total += num_of_char

print(total)
