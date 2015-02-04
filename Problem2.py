a=1
b=1
c=0
total=0
while c<4000000:
    c=a+b
    if c<4000000:
        total=total+c
    a=b+c
    b=a+c
print total
