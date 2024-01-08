# 8.1.2024
# Project Euler 001: Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

include = [3,5]
exclude = []            # This (and the code on line 19-21) is because I thought it was perhaps an exclusive OR
threshold = 1000

def count_multiples():
    sum = 0
    for count in range(threshold):
        candidate = False
        for a in include:
            if divides(count,a):
                candidate = True
        for b in exclude:
            if divides(count,b):
                candidate = False
        if candidate:
            sum += count
    return sum

def divides(x,y):
    answer = False
    if x % y == 0:
        answer = True
    return answer


if __name__ == "__main__":
    print(count_multiples())