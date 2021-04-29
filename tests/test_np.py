import unittest

import numpy as np
from calculator.advanced.numpy_functions import *


class BasicTest(unittest.TestCase):
    def test_conversion(self):
        self.assertIsInstance(list_to_numpy([1, 2, 3]), np.ndarray)

    def test_mean(self):
        self.assertEqual(average([1, 2, 3]), 2)
        self.assertEqual(average([3]), 3)


if __name__ == "__main__":
    unittest.main()
