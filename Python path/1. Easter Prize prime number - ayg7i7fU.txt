def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


n = int(input())
m = int(input())

result = find_primes(n, m)

print(' '.join(map(str, result)))
print(f"The total number of prime numbers between {n} to {m} is {len(result)}")
