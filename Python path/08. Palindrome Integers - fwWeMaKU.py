def palindrome(numbers):
    for i in numbers:
        if i == i[::-1]:
            print(f'True')
        else:
            print(f'False')


nums = input().split(", ")
palindrome(nums)
