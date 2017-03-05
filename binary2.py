number = 0
i = 0
binary = input('Input the number:')
while binary > 0:
    x=binary%10
    y= x *(2**i)
    number = number + y
    binary=binary//10
    i = i + 1
    
print number
