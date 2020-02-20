test_1 = int(input("test score one"))
if 0 > test_1 < 25:
    print("error")
test_2 = int(input("test score"))
if 0 > test_2 < 25:
    print("error")
external = int(input("external test"))
if 0 > external < 50:
    print("error")

total = test_1 + test_2 + external

if total < 50 or external < 25 :
    print("fail")

if 50 < total < 60:
    print("Pass")

if 80 > total > 60 :
    print("credit")

if total >= 80 :
    print("distinction")