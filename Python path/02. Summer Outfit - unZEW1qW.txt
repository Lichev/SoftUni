gradus = int(input())
time = input()

outfit = ""
shoes = ""

if time == 'Morning':
    if 10 <= gradus <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < gradus <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif time == 'Afternoon':
    if 10 <= gradus <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < gradus <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Swim Suit"
        shoes = "Barefoot"

elif time == 'Evening':
    if 10 <= gradus <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < gradus <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {gradus} degrees, get your {outfit} and {shoes}.")