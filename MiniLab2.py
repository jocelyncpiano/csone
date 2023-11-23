num=int(input("Enter a number: "))
new=num+1
for x in range(2, new):
    if num%x==0 and num!=x:
        print("Not a prime")
        break
else:
    print("Prime")
    