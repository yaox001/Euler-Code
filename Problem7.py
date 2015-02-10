def isPrime(a):
    k=2
    while k<=a:
            if k<a and a%k==0:
                    return False
                    break
            elif k<a:
                    k=k+1
            else:
                    return True
                
primes=[2]
i=3
"""count=2
while count<10001:
    if isPrime(i)==True:
        primes.append(i)
        count=count+1
    i=i+1
print primes[10000]"""

while len(primes)<10001:
    if isPrime(i)==True:
        primes.append(i)
    i=i+1
result=primes[10000]
print result
