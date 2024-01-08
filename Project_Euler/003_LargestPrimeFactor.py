# 8.1.2024
# Project Euler 003: Largest Prime Factor

# What is the largest prime factor of the number 600851475143?

import math


n = 600851475143

def prime(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    either_side_of_six = n % 6
    if either_side_of_six > 1 and either_side_of_six < 5:
        return False

    max = (int(math.ceil(math.sqrt(abs(n)))))

    sieve = [0]

    for s in range(max):
        sieve.append(1)

    d = 2
                                # Count up to sqrt(n)
    while d <= max:
                                # Only check a new divisor if it has not already been eliminated
        if sieve[d] == 1:
            if n % d == 0:
                return False
                                # If a number d does not divide n, then eliminate all multiples of d from the search
        for j in range(d,len(sieve),d):
            sieve[j] = 0
        d += 1

    return True


def factors(n):
    divisor = 3

    primefactorfound = False

    while primefactorfound == False:
        mod = n % divisor
        if mod == 0:
            m = int(n/divisor)
            print("Factor: " + str(m))
            if prime(m):
                print("(and that factor is PRIME)")
                return
        divisor += 1


if __name__ == "__main__":
    factors(600851475143)