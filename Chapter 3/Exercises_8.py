hot_dogs = 10
buns = 8
people = int(input("people attending"))
eating = int(input("amount per person"))
required = people * eating
h = required//hot_dogs
b = required//buns
b2 = required%buns
h2 = required%hot_dogs
print(b)
if 8 < b2:
    b + 2

elif 0 < b2:
    b+2

if h2 > 0:
    h + 1



print("The minimum number of packages of hot dogs required is", h)
print("The minimum number of packages of hot dog buns required", b)
print("The number of hot dogs that will be left over", h2)
print("The number of hot dog buns that will be left over", b2)