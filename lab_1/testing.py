import unittest
from lab1 import zig_zag_way
from lab1 import mtrx

class testing(unittest.TestCase):
    def test(self):
        exp = [[1, 2, 6],
               [3, 5, 7],
               [4, 8, 9]]
        self.assertEqual(zig_zag_way(mtrx), exp)

        zig_matrix = zig_zag_way(mtrx)
        for row in zig_matrix:
            print(row)



if __name__ == "__main__":
    unittest.main()