num=int(input("Enter a number: "))
divide = 2
while divide<num:
    if num%divide==0:
        print("Not a prime.")
        break
    else:
        divide+=1
        continue
else:
    print("Prime.")