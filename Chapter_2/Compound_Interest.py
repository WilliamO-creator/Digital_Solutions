P = float(input("the principal amount that was originally deposited into the account."))
r = float(input("the annual interest rate."))
n = float(input("the number of times per year that the interest is compounded."))
t = float(input("the specified number of years."))
intrest = r/100
num1 = n*t
A = P*(1+intrest*n)
final = num1*A
print("the amount of money in the account after the specified number of years", A)