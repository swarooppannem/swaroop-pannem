a=int(input('Enter the number 1:'))
b=int(input('Enter the number 2:'))
c=int(input('Enter the number 3:'))
if a>b:
    if a>c:
        print str(a) +' ' + 'is the largest number.'
    else:
        print str(c) +' '+ 'is the largest number.'
else:
    if b>c:
        print str(b) +' '+ 'is the largest number.'
    else:
        print str(c)+' ' + 'is the largest number.'
