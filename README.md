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
* Define and initialize an accumulator called **k**, of type integer that returns range of number of elements in a list from zero to length of lst_of_strings, incremented by 2
* use for loop to iterate over **k**  with loop variable named **i**
    * using slicing method making two strings into a sublist and storing it in a list **list_lst_nd_fstnames**
    * concatenating list_lst_nd_fstnames and using slicing making last and first name as sublist and storing it in **list_lst_nd_fstnames**
* Assign an empty dictionary to a variable of type dictionary named **result**
* use for loop to iterate over **key**  with loop variable named **keys**
    * use for loop to iterate over **value**  with loop variable named **list_lst_nd_fstnames**
         * storing the value in dictionary **result** of specified key
         * removing the value from **list_lst_nd_fstnames**
         * break the loop
* Return **result**
