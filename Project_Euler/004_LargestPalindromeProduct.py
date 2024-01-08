# 8.1.2024
# Project Euler 004: Largest Palindrome Product
#
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99 .
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome(n):
    if n//10 < 1:
        return True

    remember_n = n
    digits = []

    while n:
        digits.insert(0,n % 10)
        n //= 10

    m = 0

    for power, digit in enumerate(digits):
        m += digit * (10**power)

    if m == remember_n:
        return True
    else:
        return False


def search_for_palindromes(max):
    record = 9009
    for x in range(max):
        for y in range(max):
            product = x*y
            if palindrome(product):
                if product > record:
                    record = product
    print(record)


if __name__ == "__main__":
    search_for_palindromes(1000)