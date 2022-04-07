def is_prime(nb):
    for j in range(2, nb // 2):
        if nb % j == 0:
            return False
    return True


primes = []
for i in range(1000):
    if is_prime(i):
        primes.append(i)

print(primes)
