def isPrime(a):
    #if a==2:
     #   return True
    # elif a<=1:
    #    return False
    #else:
    k=2
    while k<=a:
        if k<a and a%k==0:
            return False
            break
        elif k<a:
            k=k+1
        else:
            return True
def lgprime(x):
    i=x-1
    largest=x
    while i>=2:
        if x%i==0 and isPrime(i)==True:
            largest=i
            print largest
            break
        else:
            i=i-2
    if largest==x and isPrime(x)==True:
        largest=x
    return largest
print lgprime(600851475143)
