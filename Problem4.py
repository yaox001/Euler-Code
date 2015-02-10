def isPalin(x):
    word=str(x)
    backwd=word[::-1]
    if word==backwd:
        return True
    else:
        return False
print isPalin(323)

largest=0
for i in range (100, 1000):
    for j in range (100,1000):
        prod=i*j
        if isPalin(prod)==True:
            if prod>largest:
                largest=prod
            else:
                j=j+1
    i=i+1
print largest
