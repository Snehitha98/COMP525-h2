### make_roster()
```
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
```
* Making all the sublists of student_list into a single list
* Assign an empty list to a variable of type list named **flat_list**
* use for loop to iterate over **student_list**  with loop variable named **sublist**
    * use for loop to iterate over **sublist**  with loop variable named **item**
        * append item to flat_list
* Storing all the keys in a list
* Assign an empty list to a variable of type list named **keys**
* using slicing, storing only student ID in a list **keys**
* assigning keys to another variable named **unwanted_numbers**
* Assign an empty list to a variable of type list named **lst_of_strings**
* use for loop to iterate over **flat_list**  with loop variable named **ele**
    * use if statement to check if **ele** is not in **unwanted_numbers**
        * concatenate **ele** to **lst_of_strings** and store it in a list **lst_of_strings**  
* Making last and first names as sublist from lst_of_strings
* Assign an empty list to a variable of type list named **list_lst_nd_fstnames**
* Define and initialize an accumulator called **k**, of type integer that returns range of number of elements in a list from zero to length of lst_of_strings, with a step value 2
* use for loop to iterate over **k**  with loop variable named **i**
    * using slicing method making two strings into a sublist and storing it in a list **list_lst_nd_fstnames**
    * concatenating list_lst_nd_fstnames and using slicing making last and first name as sublist and storing it in **list_lst_nd_fstnames**
* Assign an empty dictionary to a variable of type dictionary named **result**
* use for loop to iterate over **keys**  with loop variable named **key**
    * use for loop to iterate over **list_lst_nd_fstnames**  with loop variable named **value**
         * storing the value in dictionary **result** of specified key
         * removing the value from **list_lst_nd_fstnames**
         * break the loop
* Return **result**

### sort_roster()
```
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
```
* Assign an empty list to variable named **keys**
* use for loop to iterate over **students**  with loop variable named **key**
    * concatenating key to a list keys and storing it in a list **keys**
* Assign an empty list to variable named **values**
* use for loop to iterate over **students**  with loop variable named **key**
    * concatenating values in dictionary students of specified key to a list values and storing it in a list **values**
* Assign an empty list to variable named **lst_name**
* using string slicing accessing only last names from values and storing it in **lst_name**
* Assign an empty dictionary to a variable of type dictionary named **result**
* use for loop to iterate over **lst_name**  with loop variable named **key**
    * use for loop to iterate over **keys**  with loop variable named **value**
         * storing the value in dictionary **result** of specified key
         * removing the value from **keys**
         * break the loop
* Return **result**

### add_gpa()
```
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
```
* Making all the sublists of student_list into a single list
* Assign an empty list to a variable of type list named **flat_list**
* use for loop to iterate over **student_list**  with loop variable named **sub_list**
    * use for loop to iterate over **sub_list**  with loop variable named **ele**
        * append ele to **flat_list**
* Assigning value two to variable named **index**
* use for loop to iterate over **gpa_list**  with loop variable named **gpa**
    * insert gpa at specified index position in flat_list
    * increment index by 3
* Assign an empty list to variable named **result**
* initialize a variable named **k**, of type integer that returns range of number of elements in a list from zero to length of flat_list, with a step value 3
* use for loop to iterate over k with loop variable named **i**
    * concatenating result and slicing flat_list by making ID,last name and gpa as sublist and storing it in a list **result**
* Return **result**
