head = input()
body = input()
tail = input()

ocb = [head, body, tail]

ocb[0], ocb[2] = ocb[2], ocb[0]

print(ocb)