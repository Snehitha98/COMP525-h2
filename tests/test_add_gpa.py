"""
test_add_gpa.py
Snehitha Mamidi
February 27, 2020
"""

import unittest
from problems.practice_transformations import StudentModel


class Testaddgpa(unittest.TestCase):
    """
    Tests for add_gpa() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.sm = StudentModel()

    def test_case1_add_gpa(self):
        """
        Test case for add_gpa
        """
        input1 = [[901,'Mamidi'],[915,'Pabbathi']]
        gpa_list = [9.8, 8.1]
        actual_result = self.sm.add_gpa(input1, gpa_list)
        expected_result = [[901, 'Mamidi', 9.8], [915, 'Pabbathi', 8.1]]
        self.assertEqual(actual_result, expected_result)

    def test_case2_add_gpa(self):
        """
        Test case for add_gpa
        """
        input1 = [[999,'Bairy']]
        gpa_list = [9.8]
        actual_result = self.sm.add_gpa(input1, gpa_list)
        expected_result =  [[999, 'Bairy', 9.8]]
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
