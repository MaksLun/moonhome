numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for n in numbers:
    is_prime = True

    if n < 2:
        is_prime = False

    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)

print("Простые числа:", primes)
print("Непростые числа:", not_primes)








