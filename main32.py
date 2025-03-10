primes = []
num = 2
while len(primes) < 100:
    if is_prime(num):
        primes.append(num)
    num += 1
print("Первые 100 простых чисел:", primes)
