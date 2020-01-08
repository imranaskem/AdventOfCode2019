import unittest
import day01


class TestMyFuelCalc(unittest.TestCase):
    def test_processmass(self):
        mass = 1969
        expected = 966
        fuel = day01.processMass(mass)

        self.assertEqual(fuel, expected)


if __name__ == '__main__':
    unittest.main()
