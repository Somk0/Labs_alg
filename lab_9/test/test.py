import unittest

import sys
sys.path.append("../src")


from lab_9 import indiano


exp = 19
plates = open("ijones.in","r")
class test_ing(unittest.TestCase):
    def test(self):
        exp = 19
        self.assertEqual(main(plates), exp)


if __name__ == "__main__":
    unittest.main()
    
