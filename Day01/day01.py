import math

file = open("./input.txt")
inputs = []

for line in file:
    inputs.append(int(line))

file.close()

def calculateFuel(input):
    rounded = math.floor(input / 3)

    return (rounded - 2)

def processMass(mass):
    totalMassFuel = 0

    massFuel = calculateFuel(mass)
    totalMassFuel += massFuel

    while massFuel > 0:
        massFuel = calculateFuel(massFuel)
        totalMassFuel += massFuel

    return totalMassFuel

totalFuel = 0

for input in inputs:
    moduleFuel = processMass(input)
    totalFuel += moduleFuel

print(totalFuel)
