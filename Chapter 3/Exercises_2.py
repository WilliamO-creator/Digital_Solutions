Rectangle_1_W = int(input("wieght of triangle 1"))
Rectangle_1_L = int(input("Leaght of triangle 1"))
Rectangle_2_W = int(input("wieght of triangle 1"))
Rectangle_2_L = int(input("leaght of triangle 1"))
t1 = Rectangle_1_W * Rectangle_1_L
t2 = Rectangle_2_W * Rectangle_2_L
if t1 < t2:
    print("Rectangle 2 is bigger")

else :
    print("Rectangle 1 is bigger")
