nums = [n for n in input().split(", ")]
count = 10

while len(nums) > 0:
    nums_int = list(map(int, nums))
    numbers = [x for x in nums_int if x <= count]
    print(f"Group of {count}'s: {numbers}")
    nums_str = list(map(str, numbers))

    for i in nums_str:
        if i in nums:
            nums.remove(i)
    count += 10

