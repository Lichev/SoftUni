filter = input().split(", ")
text = input()

for word in filter:
  while word in text:

    text = text.replace(word, "*" * len(word))


print(text)