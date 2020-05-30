
import math


#check if number is even
def isEven(x):
    return x % 2 == 0


#check if number is prime
def isPrime(x):

    for i in range(2, math.sqrt(x)):
        if x % i == 0:
            return False

    return True

#check for number being factor of the other
def isFactor(number, divisor):
    return number % divisor == 0


def highestPrimeFactor(x):
    highest = -1

    # reduce down until no longer divisible by 2. If it's even and not 2, it cant be prime
    while x % 2 == 0:
        highest = 2
        x //= 2


    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            highest = i
            x //= i

    if x > 2:
        return x
    else:
        return highest


    

    return highest
