from day1 import fuelcalc

def TestProcessMass(mass, expected):
    fuel = fuelcalc.processMass(mass)

    if fuel == expected:
        print('Correct fuel')
    else:
        print('Incorrect fuel, got {0}, expected {1}'.format(fuel, expected))

TestProcessMass(1969, 966)
TestProcessMass(100756, 50346)