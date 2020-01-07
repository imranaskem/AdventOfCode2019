import fuelcalc

def TestProcessMass():
    mass = 1969
    expected = 966
    fuel = fuelcalc.processMass(mass)

    if fuel == expected:
        print('Correct fuel')
    else:
        print('Incorrect fuel, got {0}, expected {1}'.format(fuel, expected))

TestProcessMass()