Reservation = input("Welcome to Johnny Monkey's. Do you have a reservation? ")
if Reservation=="yes":
    Time = int(input("Excellent, what time? "))
Guests = int(input("How many people are dining? "))
Appetizers = int(input("How many appetizers? "))
Entrees = int(input("How many entrees? "))
Desserts = int(input("How many desserts? "))
Birthday = input("Anyone's birthday? ")
Members = input("Are you a loyalty member? ")
Level = 0
Bill = 0
Points = 0

if Birthday=="yes":
    Desserts-=1   
if Members=="yes":
    Level = input("What level? (Silver or Gold) ")
Bill = Entrees*19.99 + Appetizers*9.99 + Desserts*7.99
if Reservation=="yes":
    if Time<7:
        Bill*=0.95
    if Time>10 and Desserts>0:
        Bill-=7.99
if Guests>=6 or Entrees>=6:
    Bill*=1.2
if Level=="gold":
    Points=10*Bill
if Level=="silver":
    Points=5*Bill
Bill= round(Bill)
print("Your bill is:", Bill)
print("You earned:", Points, "points")


