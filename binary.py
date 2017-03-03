number = 0
binary = input('Input the number:')
for i in range (0,9):
    x=binary%10
    y=x*(2**i)
    number = number + y
    binary=binary//10
print number    