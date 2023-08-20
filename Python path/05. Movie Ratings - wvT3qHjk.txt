n = int(input())

movieH = ""
highest = -10

movieL = ""
lowest = 10

avarage = 0

for i in range(n):
    movie = input()
    rating = float(input())

    if rating > highest:
        movieH = movie
        highest = rating

    elif rating < lowest:
        movieL = movie
        lowest = rating
    avarage += rating


print(f"{movieH} is with highest rating: {highest:.1f}")
print(f"{movieL} is with lowest rating: {lowest:.1f}")
print(f"Average rating: {(avarage / n):.1f}")