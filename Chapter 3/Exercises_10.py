print("enter the number of coins required to make exactly one dollar")
pennies = int(input("enter number of pennies"))
nickels = int(input("enter number of nickels"))
dimes = int(input("enter number of dimes"))
quarters = int(input("enter number of quarters"))
p = 0.01
n = 0.05
d = 0.1
q = 0.25

TotalP = p*pennies
TotalN = n*nickels
TotalD = d*dimes
TotalQ = q*quarters

Total = TotalP+TotalN+TotalD+TotalQ

if Total == 1:
    print("Correct total of a dollar")

else:
    print("you are have the amount incorrect by", Total - 1)
