sum=0
for x in range (4,6):
    for y in range (1,5):
        if (x+y)%2==1:
            continue
        else:
            sum+=y
            print(y)
            print(sum)
else:
    sum-=5
print(sum)