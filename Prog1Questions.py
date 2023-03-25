'''Objective: Find the smallest positive number that is evenly divisible by all the numbers from 1-20'''

import math as m

def minPosNum():
    res = 1
    for i in range(1, 21):  # Iterates through the range 1-20
        x = (i // m.gcd(i, res))  # i floor divided by the greatest common divisor of i and res (which starts at 1)
        res *= x  # result is multiplied by result * x
    return res  # returns solution at the end of for loop iteration


print(f"Smallest: {minPosNum()}")

'''Takes a list of numbers, a starting base, and a target base - then converts the numbers in the starting base
    to a number in the target base'''

def convertBase(ls, b1, b2):
    '''Converts the list of numbers to base 10'''
    b10List = []
    for i in range(0, len(ls)): #Iterates through list of numbers
        if ls[i] < 0:   #Converts number to positive if entered negative
            ls[i] *= -1
        b10num = int(str(ls[i]), b1)    #Converts number to base 10
        b10List.append(b10num)
    '''Converts the base 10 number list to the target base'''
    targetList = []
    for i in range(0, len(b10List)):    #Iterates through new base 10 list of numbers
        while b10List[i]:   #Converts from base 10 -> target base using method found below
            targetList.append(int(b10List[i] % b2))
            b10List[i] //= b2
    return targetList[::-1]

def main():
    try:
        ls = [int(x) for x in input('Enter the list of numbers: ').split()] #Creates a list out of entered numbers
        b1 = int(input('Enter starting base: '))
        b2 = int(input('Enter target base: '))

        print('Original List:', ls)
        print('New List:', convertBase(ls, b1, b2))
    except ValueError:
        print('ERROR: One or more of the numbers you entered exceeded the bounds of your starting base :(')

main()

'''Converting from B10 to target base::
1. Divide the number by the base
2. Take the remainder and append it to the list
3. Repeat division using whole number quotient we got from the previous division
4. Continue division until quotient is 0 (but still append the remainder)
5. Answer of the remainders read bottom-up'''

'''Objective: Find the largest prime factor of 600851475143'''

import math

n = 600851475143
maxFactor = []
for i in range(2, math.ceil(math.sqrt(n))): #From 2 -> square root of number
    while n % i == 0:   #Checks if numbers are divisible by anything else
        maxFactor.append(i) #If so, adds them to the list
        n /= i

print(f"Largest prime factor of {n}: {maxFactor[-1]}")    #Ensures that only the max factor is returned, not other ones