book_name = input()
current_book = input()

count = 0
book_found = False

while current_book != 'No More Books':

    if current_book == book_name:
        book_found = True
        break
    count += 1
    current_book = input()

if book_found:
    print(f"You checked {count} books and found it.")
else:
    print(f'The book you search is not here!')
    print(f'You checked {count} books.')
