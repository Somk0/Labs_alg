import unittest

import sys
sys.path.append("../src")

from lab_8 import minimal_cable_length

ilands = open(r'islands.csv')
ilands1 = open(r'islands1.csv')

class testing(unittest.TestCase):
    def test(self):
        exp = 19
        self.assertEqual(minimal_cable_length(ilands1), exp)


if __name__ == "__main__":
    unittest.main()
    
