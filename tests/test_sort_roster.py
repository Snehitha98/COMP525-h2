"""
test_sort_roster.py
Snehitha Mamidi
February 27, 2020
"""

import unittest
from problems.practice_transformations import StudentModel


class TestSortRoster(unittest.TestCase):
    """
    Tests for sort_roster() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.sm = StudentModel()

    def test_case1_sort_roster(self):
        """
        Test case for sort_roster
        """
        input1 = {901:['Mamidi','Snehitha'],915:['Pabbathi','Harshitha']}
        actual_result = self.sm.sort_roster(input1)
        expected_result = {'Mamidi': 901, 'Pabbathi': 915}
        self.assertDictEqual(actual_result, expected_result)

    def test_case2_sort_roster(self):
        """
        Test case for sort_roster
        """
        input1 = {917:['Neela','Pavani'],930:['Bairy','Harini'],904:['Anumala','Amulya'],981:['Gajjula','manoj']}
        actual_result = self.sm.sort_roster(input1)
        expected_result = {'Neela': 917, 'Bairy': 930, 'Anumala': 904, 'Gajjula': 981}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
