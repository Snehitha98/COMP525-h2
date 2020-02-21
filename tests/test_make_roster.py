"""
test_parse_make_roster.py
Mihaela
Created February 20, 2020
"""

import unittest
from problems.practice_transformations import StudentModel


class TestMakeRoster(unittest.TestCase):
    """
    Tests for make_roster() method
    """
    def setUp(self):
        """
        Define attribute p to hold object of type Problems
        """
        self.sm = StudentModel()

    def test_two_element_roster(self):
        """
        Test case for a 2-element roster
        """
        input1 = [
            [901, 'adams'],
            [902, 'bennett']
        ]
        actual_result = self.sm.make_roster(input1)
        expected_result = {901: 'adams', 902: 'bennett'}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
