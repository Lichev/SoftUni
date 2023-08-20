def valid_password(password):
    firs_valid = False
    second_valid = password.isalnum()
    count = 0
    third_valid = False

    if 6 <= len(password) <= 10:
        firs_valid = True
    else:
        print(f'Password must be between 6 and 10 characters')

    if not second_valid:
        print(f'Password must consist only of letters and digits')

    for i in range(len(password)):
        if password[i].isdigit():
            count += 1
        if count >= 2:
            third_valid = True
            break
    if not third_valid:
        print(f"Password must have at least 2 digits")

    if firs_valid and second_valid and third_valid:
        print(f'Password is valid')


vhod = input()
valid_password(vhod)
