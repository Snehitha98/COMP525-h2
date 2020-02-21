"""
h2.py
(enter your name)
(enter date)
"""


class StudentModel:
    """
    Utility class with a series of data structure transformation methods
    of possible interest to student-related data applications
    """

    def make_roster(self, student_list):
        """
        Parses student_list to create a dictionary keyed by student ID
        student_list: list of sublists, where a sublist has three
        positional items:
            student ID - 3-digit integer starting with digit 9
            last name - alphabetic string
            first name - alphabetic string
        Returns: dictionary
            keys are student IDs
            values are lists of two positional items
                last name and first name - alphabetic strings
        """
        pass

    def sort_roster(self, students):
        """
        Parses students to create a dictionary keyed by student last name
        students: dictionary
            keys are student IDs
            values are lists of two positional items, last name and first name
        Returns: dictionary
            keys are last names
            values are student IDs that correspond to that last name
        """
        pass

    def add_gpa(self, student_list, gpa_list):
        """
        Parses the two parallel lists, student_list and gpa_list to create
        a new list of sublists
        student_list: list of sublits, where a sublist has two
        positional items
            student ID - 3-digit integer starting with digit 9
            last name - alphabetic string
        Returns: list of sublists, where a sublist has three positional items:
            student ID - 3-digit integer (from student_list sublists)
            last name - string (from student_list sublists)
            gpa - decimal number (from gpa_list)
        """
        pass

    def gpa_histogram(self, student_list):
        """
        Parses student_list to create a histogram of student GPAs
        student_list: list of sublists, where a sublist has three
        positional items:
            student ID - 3-digit integer starting with digit 9
            last name - alphabetic string
            gpa - decimal number
        Returns: dictionary
            keys: converted gpa values from the student_list into
                positive integers
            values: frequency of the gpa values in the student list
        """
        pass


if __name__ == '__main__':
    sm = StudentModel()
    # Write test cases for all four functions
