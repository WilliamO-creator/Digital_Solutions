test_1 = int(input("test score one"))
test_2 = int(input("test score"))
external = int(input("external test"))
total = test_1 + test_2 + external
if total < 60:
    print("Pass")

if total >