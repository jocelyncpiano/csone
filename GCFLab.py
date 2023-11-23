integer1=int(input("Enter a number: "))
integer2=int(input("Enter another numer: "))
remainder = 1
while (remainder != 0):
    remainder=integer1%integer2
    if remainder==0:
        print("The GCF is", integer2)
    else:
        integer1=integer2
        integer2=remainder