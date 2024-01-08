# 8.1.2024
# Project Euler 005: Smallest Multiple
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divisors = [2,3,4,5,7,9,11,13,16,17,19]
# (12, 15, 20 etc already covered by 3*4, 2*5, 4*5 etc)

def does_it_divide(n):
    for d in divisors:
        if n % d != 0:
            return False

    return True


if __name__ == "__main__":
    n = 2520
    while not does_it_divide(n):
        n += 1

    print (n)

