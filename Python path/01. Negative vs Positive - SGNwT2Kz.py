def sort_numbers(*args):
    def negatives():
        negative_list = []
        for x in args:
            if x < 0:
                negative_list.append(x)
        return negative_list

    def postives():
        postive_list = []
        for x in args:
            if x > 0:
                postive_list.append(x)
        return postive_list

    print(sum(negatives()))
    print(sum(postives()))

    abs_of_positives = abs(sum(postives()))
    abs_of_negatives = abs(sum(negatives()))

    if abs_of_positives > abs_of_negatives:
        print(f"The positives are stronger than the negatives")
    else:
        print(f"The negatives are stronger than the positives")


nums = list(map(int, input().split()))
sort_numbers(*nums)
