import time
speed = int(input("Speed"))
timeoftravil = int(input("Time in hours"))

t = 0
while t < timeoftravil:
    t = t + 1
    d = speed * t
    time.sleep(2)
    print("After", t, "hours you will have traviled", d, "Kilmeters")