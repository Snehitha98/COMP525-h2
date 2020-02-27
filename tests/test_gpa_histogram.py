"""
test_gpa_histogram.py
Snehitha Mamidi
February 27, 2020
"""

import unittest
from problems.practice_transformations import StudentModel


class TestGpaHistogram(unittest.TestCase):
    """
    Tests for gpa_histogram() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.sm = StudentModel()

    def test_case1_gpa_histogram(self):
        """
        Test case for gpa_histogram
        """
        input1 = [[901,'Mamidi',9.01],[915,'Pabbathi',8.2],[915,'Padidam',9.9],[915,'Neela',7.2]]
        actual_result = self.sm.gpa_histogram(input1)
        expected_result = {9: 2, 8: 1, 7: 1}
        self.assertDictEqual(actual_result, expected_result)

    def test_case2_gpa_histogram(self):
        """
        Test case for gpa_histogram
        """
        input1 = [[901,'Mamidi',6.3],[915,'Pabbathi',6.9],[915,'Padidam',6.01],[915,'Neela',6.12],[900,'Podamekala',4.3]]
        actual_result = self.sm.gpa_histogram(input1)
        expected_result = {6: 4, 4: 1}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
