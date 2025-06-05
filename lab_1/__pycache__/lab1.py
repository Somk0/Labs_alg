
import unittest

def zig_zag_way(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * cols for _ in range(rows)] 
    step = 1

    for diag in range(rows + cols - 1):

        if diag < cols: 
            one_row = 0
            one_col = diag

        else:
            one_row = diag - cols + 1
            one_col = cols - 1

        diagonal_element = []

        while one_row < rows and one_col >= 0:
            diagonal_element.append((one_row, one_col))

            one_row += 1
            one_col -= 1

        if diag % 2 == 0:
            diagonal_element = diagonal_element[::-1]
        
        for (r, c) in diagonal_element:
            result[r][c] = step
            step += 1
        
    return result


mtrx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

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