countries = input().split(", ")
capitals = input().split(", ")
zipped = zip(countries, capitals)


[print(key, "->", value) for key, value in zipped]