total=0
sumsqr=0
sqrsum=0
for i in range (1,101):
    total=total+i
    sumsqr=sumsqr+i**2
    sqrsum=total**2
print sqrsum-sumsqr
