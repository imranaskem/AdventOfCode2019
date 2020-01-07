from day1 import fuelcalc

file = open("input.txt")
inputs = []

for line in file:
    inputs.append(int(line))

file.close()

totalFuel = 0

for input in inputs:
    moduleFuel = fuelcalc.processMass(input)
    totalFuel += moduleFuel

print(totalFuel)
