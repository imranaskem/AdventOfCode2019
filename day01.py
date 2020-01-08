import math
import utils


def calculateFuel(input):
    rounded = math.floor(input / 3)

    return (rounded - 2)


def processMass(mass):
    totalMassFuel = 0

    massFuel = calculateFuel(mass)
    totalMassFuel += massFuel

    while massFuel > 0:
        massFuel = calculateFuel(massFuel)
        if massFuel > 0:
            totalMassFuel += massFuel

    return totalMassFuel


inputs = utils.load_text_file("inputs/day01.txt", __file__)

totalFuel = 0

for input in inputs:
    moduleFuel = processMass(input)
    totalFuel += moduleFuel

print(totalFuel)
