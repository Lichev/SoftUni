word1 = input()
word2 = input()

for i in range(len(word1)):

    if word1[i] != word2[i]:
        replacement = word2[i]

        word = word1[0:i] + replacement + word1[i + 1:]
        word1 = word
        print(word1)
