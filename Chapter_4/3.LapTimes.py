
laps = int(input("how many laps have you done"))
i = 0
times = set()
laptime = 0
def MAX(times):
    return (max(times))
def Min(times):
    return (min(times))
def averageOfList(times):
    sumOfNumbers = 0
    for t in times:
        sumOfNumbers = sumOfNumbers + t

    avg = sumOfNumbers / len(times)
    return avg
while i < laps:
    time = int(input("enter your time for your lap"))
    i = i + 1
    times.add(time)
print("The fastest time is ", Min(times))
print("The slowest time is ", MAX(times))
print("Avrage lap time is ", averageOfList(times))