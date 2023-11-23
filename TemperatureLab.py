temp=int(input("What is the temperature outside? "))
cleats=input("Did you bring cleats? (Y/N) ")
suit=input("Did you bring your swimsuit? ")
print("Looks good for...")
if 80<=temp<=95:
    print("Suntanning")
if temp>=75:
    print("Swimming")
if 10<temp<=32:
    print("Skiing")
if temp<=10:
    print("Checkers")
if 32<temp<=70:
    print("soccer")
if 40<=temp<=80:
    print("pickleball")
    