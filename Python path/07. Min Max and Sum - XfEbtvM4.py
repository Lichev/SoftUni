def minimum(numbers):
    return min(numbers)


def maximum(numbers):
    return max(numbers)


def summed(numbers):
    return sum(numbers)


nums = [int(x) for x in input().split(" ")]
print(f"The minimum number is {minimum(nums)}")
print(f"The maximum number is {maximum(nums)}")
print(f"The sum number is: {summed(nums)}")
