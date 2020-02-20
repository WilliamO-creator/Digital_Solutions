R = int(input("length of the row, in feet."))
E = int(input("amount of space, in feet, used by an end-post assembly."))
S = int(input("the space between vines, in feet."))
V = (R-2*E)/S
print("the number of grapevines that will fit in the row",V)