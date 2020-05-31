import NumberCheck

#sum of multiples of 3 or 5 below 1000
def problem1():
    sum = 0

    for i in range(0,1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    print(sum)

#Summing the even fibonacci numbers up to 4000000
def problem2():
    
    sum = 0

    #starting with 1 and 1 in the sequence
    a = 1 #first number for fib addition
    b = 1 #second number for fib addition
    c = 0 

    Flag = True

    while(Flag):
           if (a+b < 4000000):
               c = a + b
               if (NumberCheck.isEven(c)):
                   sum += c

               a = b
               b = c
           else:
                Flag = False

    print(sum)


#find largest prime factor of given number 600851475143
def problem3(x):

    result = NumberCheck.highestPrimeFactor(x)

    print(result)


#lowest number that is evenly divded by the numbers 1-20
def problem5():
    found = False

    #the problem stated that 2520 was the number divisible by the numbers 1-10 so I know my number is going to be a
    #multiple of this number. I can start here and increment by this number to cut down on total numbers analyzed
    i = 2520

    while (not found):
        #only need to look at certain numbers rather than all 1-20 since I know, for example, if a number is divisble
        #by 20, it is also divisible by 10, 2, etc.

        # I started with 11-20 but really I only need to look at the primes between 1-20 and 20 itself
        if (i % 20 == 0) and (i % 19 == 0) and (i % 18 == 0) and (i % 17 == 0) and (i % 16 == 0) and (i % 15 == 0) and (i % 14 == 0) and (i % 13 == 0) and (i % 12 == 0) and (i % 11 == 0):
            found = True
        else:
            i += 2520

    print(i)


def problem6(x):

    squareOfSum = (int(x+1)*int(x/2)) ** 2

    sumOfSquare = 0

    for i in range(1, (x+1)):
        sumOfSquare += (i ** 2)

    print(squareOfSum - sumOfSquare)
