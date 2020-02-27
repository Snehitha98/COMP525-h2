"""
h2.py
Snehitha Mamidi
February 25, 2020
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
        flat_list = []
        for sublist in student_list:
            for item in sublist:
                flat_list.append(item)
        keys = []
        keys = flat_list[0:len(flat_list):3]
        unwanted_numbers = keys
        lst_of_strings = []
        for ele in flat_list:
            if ele not in unwanted_numbers:
                lst_of_strings = lst_of_strings + [ele]
        list_lst_nd_fstnames = []
        k = range(0,len(lst_of_strings),2)
        for i in k:
            list_lst_nd_fstnames = list_lst_nd_fstnames + [lst_of_strings[i:i+2]]
        result = {}
        for key in keys:
            for value in list_lst_nd_fstnames:
                result[key] = value
                list_lst_nd_fstnames.remove(value)
                break
        return result

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
        keys = []
        for key in students:
            keys += [key]
        values = []
        for key in students:
            values = values + students[key]
        lst_name = []
        lst_name = values[0:len(values):2]
        result = {}
        for key in lst_name:
            for value in keys:
                result[key] = value
                keys.remove(value)
                break
        return result

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
    student_list = [[901,'Mamidi','Snehitha'],[915,'Pabbathi','Harshitha']]
    result = sm.make_roster(student_list)
    print(f'(make_roster{student_list}) returns {result}')
    # Test case for make_roster()
    student_list = [[999,'Padidam','Pushyami']]
    result = sm.make_roster(student_list)
    print(f'(make_roster{student_list}) returns {result}')


    students = {901:['Mamidi','Snehitha'],915:['Pabbathi','Harshitha']}
    result = sm.sort_roster(students)
    print(f'(sort_roster{students}) returns {result}')
    # Test case for sort_roster()
    students = {917:['Neela','Pavani'],930:['Bairy','Harini'],904:['Anumala','Amulya'],981:['Gajjula','manoj']}
    result = sm.sort_roster(students)
    print(f'(sort_roster{students}) returns {result}')



    student_list = [[901,'Mamidi'],[915,'Pabbathi']]
    gpa_list = [10, 9.8]
    result = sm.add_gpa(student_list,gpa_list)
    print(f'(add_gpa{student_list},{gpa_list}) returns {result}')


    student_list = [[901,'Mamidi',9.01],[915,'Pabbathi',8.2],[915,'Padidam',9.9],[915,'Neela',7.2]]
    result = sm.gpa_histogram(student_list)
    print(f'(gpa_histogram{student_list}) returns {result}')
