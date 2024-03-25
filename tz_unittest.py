import unittest
import math

from tz_library import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), math.pi * 9)

if __name__ == '__main__':
    unittest.main()