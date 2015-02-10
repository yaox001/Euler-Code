"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""


"""def isPrime(x):
    i=1
    result=True
    while i<=x:
        if i<x:
            if x%i==0:
                result=False
            else:
                i=i+1
    print result
    
        
isPrime(8)"""
def isPrime(x):
    result=True
    for i in range (2,x):
        if x%i==0:
            result=False
            break
    print result
    
isPrime(600851475143)
    
