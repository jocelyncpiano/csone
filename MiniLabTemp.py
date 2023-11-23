import random
num = 1
while num<=10:
    temp = random.randint(15, 100)
    print("It is", temp, "degrees Fahrenheit outside.")
    if 15<=temp<=32:
        print("It is winter.")
    if 33<=temp<=50:
        print("It is spring.")
    if 51<=temp<=75:
        print("It is fall.")
    if 76<=temp<=100:
        print("It is summer.")
    num+=1