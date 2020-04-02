TPYear = int(input("enter number of years"))
x = 0
add = 0
while x < TPYear:
    x = x + 1
    month = 0
    while month < 12:
        month = month + 1
        rain = int(input("Rain for the month"))
        add = add + rain
print("The Avrage rain fall for", TPYear, "years is", add/(TPYear*12), "ml")