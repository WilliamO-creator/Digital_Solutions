num1 = input("enter number from 0 to 36")

g = 0
red_1 = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39)
black_1 = (2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 30, 32, 34, 36)

if num1 == '2' or '4' or '6' or 8 or 10 or 11 or 13 or 15 or 17 or 20 or 22 or 24 or 26 or 28 or 30 or 32 or 34 or 36 or 38:
    print("black")

elif num1 == '1' or '3' or '5' or '7' or 9 or 12 or 14 or 16 or 18 or 19 or 21 or 23 or 25 or 27 or 29 or 31 or 33 or 35 or 37 or 39:
    print("Red")

elif num1 == 0:
    print("Green")

else:
    print("erroExercise_10r")