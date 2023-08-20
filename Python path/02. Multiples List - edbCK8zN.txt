factor = int(input())
count = int(input())

sum = factor * count
mylist = list()

for i in range(factor , sum + 1, +factor):

    mylist.append(i)

print(mylist)