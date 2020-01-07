import math

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