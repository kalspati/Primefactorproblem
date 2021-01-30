# Initialize a list
primes = []
#find the sum of any give amount of prime numbers
def primeSum(number_of_Primes):
    for possiblePrime in range(2, 10000000):
        
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        #add found prime numbers to initialized list and return the sum of the list
        if isPrime:
            primes.append(possiblePrime)
        if len(primes) == number_of_Primes:
            Sum = sum(primes)
            break
    return Sum

#get the last 3 digits of the sum
digitList = list(str(primeSum(100003)))
threeDigit = ''
for num in [-3,-2,-1]:
    threeDigit = threeDigit + digitList[num]
threeDigit = int(threeDigit)
print(threeDigit)

#find the prime factors and the largest prime factor
factorList = []
for divisor in [2,3,5,7]:
    while threeDigit % divisor == 0:
        if threeDigit/divisor != 0:
            factorList.append(divisor)
            threeDigit = threeDigit/divisor
        if threeDigit % 3 != 0:
            factorList.append(threeDigit)
print(factorList)
print(max(factorList))
    
    


