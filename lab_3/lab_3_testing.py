import unittest
from lab_3 import binary_tree, branch_bums



class TestBranchBums(unittest.TestCase):
    def test_1(self):
       
        root = binary_tree(3)
        root.left = binary_tree(9)
        self.assertEqual(branch_bums(root), 9)

    def test_2(self):
       
        root = binary_tree(3)
        root.right = binary_tree(20)
        self.assertEqual(branch_bums(root), 0)

    def test_3(self):
       
        root = binary_tree(3)
        root.left = binary_tree(9)
        root.right = binary_tree(20)
        root.right.left = binary_tree(15)
        root.right.right = binary_tree(7)
        self.assertEqual(branch_bums(root), 24)

    def test_4(self):
        
        self.assertEqual(branch_bums(None), 0)

    def test_5(self):
        
        root = binary_tree(1)
        root.left = binary_tree(2)
        root.right = binary_tree(3)
        root.left.left = binary_tree(4)
        root.left.right = binary_tree(5)
        root.left.left.left = binary_tree(6)
        self.assertEqual(branch_bums(root), 6)

if __name__ == "__main__":
    unittest.main()