for x in range(6):
    for y in range(8):
        if (x+y)%2==0:
            print("A", end ="")
        else:
            print("B", end ="")
    print()