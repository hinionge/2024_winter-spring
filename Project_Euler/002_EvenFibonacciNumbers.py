# 8.1.2024
# Project Euler 002: Even Fibonacci Numbers

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def next_Fibonacci(tercet):
    next = tercet[1] + tercet[2]
    tercet[0] = tercet[1]
    tercet[1] = tercet[2]
    tercet[2] = next
    return tercet

def Fibonacci():
    f = 1
    tercet = [0,0,1]
    even_sum = 0

    while f < 4000000:
        tercet = next_Fibonacci(tercet)
        f = tercet[2]

                            # Check for even; add to running total
        if f % 2 == 0:
            even_sum += f

    print(even_sum)

if __name__ == "__main__":
    Fibonacci()