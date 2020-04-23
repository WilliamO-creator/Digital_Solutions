
loan_payment = int(input("loan Payment for car"))
insurance = int(input("insurcance for car each month"))
gas = int(input("gas for each month"))
oil = int(input("oil cost for money"))
tires = int(input("tires cost each month"))
maintenance = int(input("maintance cost"))
monthly = loan_payment+insurance+gas+oil+tires+maintenance
print("monthly cost $",monthly)
print("annual cost $",monthly*12)

#Write a program that asks the user to enter the monthly costs for the following expenses
#incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
#maintenance. The program should then display the total monthly cost of these expenses,
#and the total annual cost of these expenses.