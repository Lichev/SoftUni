from collections import deque

sequence_of_eggs = deque(input().split(", "))
sequence_of_pieces = deque(input().split(", "))

filled_boxes = 0

while sequence_of_eggs and sequence_of_pieces:
    first_eggs = int(sequence_of_eggs.popleft())
    piece_of_paper = int(sequence_of_pieces.pop())

    if first_eggs <= 0:
        sequence_of_pieces.append(piece_of_paper)
        continue

    if first_eggs == 13:
        first_paper = sequence_of_pieces.popleft()
        sequence_of_pieces.append(first_paper)
        sequence_of_pieces.appendleft(piece_of_paper)

    elif first_eggs + piece_of_paper <= 50:
        filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if sequence_of_eggs:
    print(f"Eggs left: {', '.join(sequence_of_eggs)}")
if sequence_of_pieces:
    print(f"Pieces of paper left: {', '.join(map(str,sequence_of_pieces))}")