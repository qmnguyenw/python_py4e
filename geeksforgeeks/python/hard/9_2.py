Listing out directories and files in Python



The following is a list of some of the important methods/functions in Python
with descriptions that you should know to understand this article.

  1.  **len()** – It is used to count number of elements(items/characters) of iterables like list, tuple, string, dictionary etc.
  2.  **str()** – It is used to transform data value(integers, floats, list) into string.
  3.  **abspath()** – It returns the absolute path of the file/directory name passed as an argument.
  4.  **enumerate()** – Returns an enumerate object for the passed iterable that can be used to iterate over the items of iterable with an access to their indexes.
  5.  **list()** – It is used to create a list by using an existing iterable(list, tuple, dictionary, set).
  6.  **listdir()** – It is used to list the directory contents. The path of directory is passed as an argument.
  7.  **isfile()** – It checks whether the passed parameter denotes the path to a file. If yes then returns **True** otherwise **False**
  8.  **isdir()** – It checks whether the passed parameter denotes the path to a directory. If yes then returns **True** otherwise **False**
  9.  **append()** – It is used to append items on list.

Please see the below code executed on interactive Python terminal to have a
quick walk through on the usages of above functions/methods.

 __

 __  
 __

 __

 __  
 __  
 __

>>> nums = [1,2,3,4,5] # list

>>> name = "Alexander"

>>> details = {"name": "Hemkesh", "age": 23,
"active": True}

>>> 

>>> # Using len()

... 

>>> len(nums)

5

>>> len(name)

9

>>> len(details)

3

>>> 

>>> # Using str()

... 

>>> str(12)

'12'

>>> str(nums)

'[1, 2, 3, 4, 5]'

>>> str(details)

"{'active': True, 'age': 23, 'name': 'Hemkesh'}"

>>> 

>>> # Using abspath()

... 

>>> import os

>>> os.listdir(".")

['Django', 'Prep', 'python-the-snake']

>>> os.path.abspath("./Django") # pass ".\Django" on windows

'/Users/admin/projects/Python/Django'

>>> os.path.abspath("Django")

'/Users/admin/projects/Python/Django'

>>> 

>>> # Using enumerate()

...

>>> enumerate(nums)

<enumerate object at 0x100620b90>

>>> 

>>> for index, item in enumerate(nums):

... print index, item

... 

0 1

1 2

2 3

3 4

4 5

>>> 

>>> # Using list()

...

>>> list()

[]

>>> list(details )

['active', 'age', 'name']

>>> list(name)

['A', 'l', 'e', 'x', 'a', 'n', 'd', 'e',
'r']

>>> 

>>> # Using isfile() & isdir()

... 

>>> os.path.isdir("Django")

True

>>> os.path.isfile("Django")

False

>>>

>>> os.path.isdir("./python-the-snake/README.md")

False

>>> os.path.isfile("./python-the-snake/README.md")

True

>>> 

>>> # Using append()

...

>>> nums.append(12)

>>> nums

[1, 2, 3, 4, 5, 12]

>>> nums.append(67)

>>> nums

[1, 2, 3, 4, 5, 12, 67]

>>> 

>>> # Don't press "Run on IDE" button available on right. You will get
error 

... # as the statements are already executed on interactive terminal.

...

>>>  
  
---  
  
 __

 __

 **Path structure on different OS**  
Windows uses **\** (back slash) as a path separator, eg. **C:\Users\Desktop\**  
Linux based system like MAC OS X, Linux uses **/** (forward slash), eg.
**/Users/Desktop/**

Let’s have a quick overview the working of above methods and functions as we
are using this in our final program.

 __

 __  
 __

 __

 __  
 __  
 __

# Python version : 2.7.12

 

# len()

# To count number of items in a list

# To count number of characters in a string

evens = [ 2, 34, 6, 8, 10]

print len(evens)

 

city = "Bangalore"

print len(city), "\n"

 

# str() : Converting into string representation

odds = [ 1, 3, 67, 45, 83, 59]

year = 2017

 

print odds

print str(odds) + " A list.\n"

print year

print str(year) + " A year.\n"

 

 

# enumerate() : iterating over index & value of a list

for (index, item) in enumerate(odds):

 print index, item

 

 

# abspath() : Getting absolute path of passed argument(path)

import os

absolute_path = os.path.abspath(".")

print "\n", absolute_path, "\n"

 

 

# isdir() : To check if passed argument is valid directory path

answer = os.path.isdir("/Users/admin/Desktop/js")

print answer

 

 

# isfile() : To check if the passed argument is valid file path

answer = os.path.isfile("/Users/admin/Desktop/js/array.js")

print answer, "\n"

 

 

# list() : To create list

details = { "name":"Rojert Rendrick", "age":24,
"city":"Bangalore" }

keys = list( details )

print keys, "\n"

 

# append() : Appending items to list

print evens

evens.append(98)

evens.append(64)

print evens, "\n"

 

# repetition operator(*) on strings

print "Python"*3

print "#"*20  
  
---  
  
 __

 __

Output:

  

  

    
    
    5
    9 
    
    [1, 3, 67, 45, 83, 59]
    [1, 3, 67, 45, 83, 59] A list.
    
    2017
    2017 A year.
    
    0 1
    1 3
    2 67
    3 45
    4 83
    5 59
    
    /Users/admin/projects/Python/PythonFiles 
    
    True
    True 
    
    ['city', 'age', 'name'] 
    
    [2, 34, 6, 8, 10]
    [2, 34, 6, 8, 10, 98, 64] 
    
    PythonPythonPython
    ####################
    

There are number of Python files & directories inside
**/Users/admin/projects/Python/PythonFiles** , we will list out all these.

Suppose current working directory is
**/Users/admin/projects/Python/Django/E-Commerce-projects/ecommerce-2/src** ,
which has some files and folders inside it.

In your case, it will be different. You will only need to pass the exact path
of the directory that you want to list out.

The following is the python code to display all the files and directories
based on the passed absolute or relative path.

If path is not specified in the calling statement then the contents of current
working directory will be displayed.

 __

 __  
 __

 __

 __  
 __  
 __

# This Python code is for Python version : 2.7.12

 

def show_directories(dir_list, path):

 """ A function that lists the directories """

 import os

 s = "%s%d%s"%("\n", len(dir_list), " directories of "
+ os.path.abspath(path))

 l = len(s)

 print s

 print "="*l

 for index, dir in enumerate(dir_list):

 print str(index+1) + ") ", dir

 

 

def show_files(file_list, path):

 """ A function that lists the files """

 

 import os

 s = "%s%d%s"%("\n", len(file_list), " files of " +
os.path.abspath(path))

 l = len(s)

 print s

 print "="*l

 for index, file in enumerate(file_list):

 print str(index+1) + ") ", file

 

 

def show_cwd_contents( path="." ):

 # A function that calls 2 functions to separately 

 # listing out directories and files.

 # It takes a default argument as cwd(.). We can 

 # pass other paths too.

 import os

 

 f_list = []

 d_list = list()

 

 try:

 for f in os.listdir(path):

 if os.path.isfile(os.path.join(path, f)):

 f_list.append(f)

 else:

 if os.path.isdir(os.path.join(path, f)):

 d_list.append(f)

 except:

 print "\nError, once check the path"

 return

 

 show_files(f_list, path)

 

 show_directories(d_list, path)

 

 

if __name__ == "__main__":

 

 # If this module is imported in other module then 

 # we need to separately call show_cwd_contents() Or 

 # show_cwd_contents(path).

 show_cwd_contents()

 show_cwd_contents("/Users/admin/projects/Python/PythonFiles")  
  
---  
  
 __

 __

Output:

    
    
    5 files of /Users/admin/projects/Python/Django/E-Commerce-projects/ecommerce-2/src
    ===================================================================================
    1)  .gitignore
    2)  db.sqlite3
    3)  manage.py
    4)  requirements.txt
    5)  todo.txt
    
    5 directories of /Users/admin/projects/Python/Django/E-Commerce-projects/ecommerce-2/src
    =========================================================================================
    1)  ecommerce2
    2)  newsletter
    3)  products
    4)  static_in_pro
    5)  templates
    
    70 files of /Users/admin/projects/Python/PythonFiles
    =====================================================
    1)  2_list_iterators.py
    2)  app.py
    3)  class_script_exec.py
    4)  class_variables.py
    5)  date_and_time.py
    6)  datetime.txt
    7)  dict.py
    8)  dictionary.py
    9)  django_home.html
    10)  error_handling.py
    11)  error_handling_output.py
    12)  error_handling_output.txt
    13)  execution_pickle.py
    14)  fb_task.py
    15)  for.py
    16)  gfg_sum_of_primes_in_numbers.py
    17)  hackerrank_numbers.py
    18)  hck_addition_aint_simple.py
    19)  hck_biased_chandan.py
    20)  hck_c_counts.py
    21)  hck_c_counts2.py
    22)  hck_c_counts3.py
    23)  hck_cool_numbers.py
    24)  hck_earth_fans.py
    25)  hck_earth_fans_2.py
    26)  hck_earth_fans_3.py
    27)  hck_earth_fans_final_on_28_dec_2016.py
    28)  hck_Little_Jhool_and_psychic_powers.py
    29)  hck_lonely_monk.py
    30)  hck_lonely_monk_orig.py
    31)  hck_maximum_AND.py
    32)  hck_min_max_problem.py
    33)  hck_monk_and_power_of_time.py
    34)  hck_numbers_rotation.py
    35)  hck_palindomic_numbers.py
    36)  hck_print_hackerearth.py
    37)  hck_print_hackerearth_2_way.py
    38)  hck_range_query.py
    39)  hck_recursive_functions.py
    40)  hck_recursive_sums.py
    41)  hck_strange_addition.py
    42)  hck_sum_of_numbers.py
    43)  interactive_img_resolutions.txt
    44)  json.py
    45)  json.pyc
    46)  katyperry.py
    47)  lambda_expression.py
    48)  linked_list_delete_nodes_at_front.py
    49)  linked_list_delete_nodes_at_front_output.txt
    50)  linked_list_is_palindrome_gfg.py
    51)  linked_list_is_palindrome_gfg_output.text
    52)  linked_list_is_palindrome_gfg_testing.py
    53)  linked_list_node_deletion_from_any_position.txt
    54)  linked_list_node_deletion_from_end.py
    55)  linked_list_node_deletion_from_end_output.txt
    56)  linked_list_node_deletion_from_middle.py
    57)  linked_list_node_insertion_at_beginning.py
    58)  linked_list_node_insertion_at_end.py
    59)  linked_list_node_insertion_at_middel_output.txt
    60)  linked_list_node_insertion_at_middle.py
    61)  map.py
    62)  merge_lists.py
    63)  mufeez_android_interview.py
    64)  python_for_loops.py
    65)  python_for_loops2.py
    66)  remove_dupliates.py
    67)  show_dir_and_files.py
    68)  show_dir_and_files_test.py
    69)  smarika_urllib_python2.7.10.py
    70)  while.py
    
    2 directories of /Users/admin/projects/Python/PythonFiles
    ==========================================================
    1)  socket_programming
    2)  wx
    

This article is contributed by **Rishikesh Agrawani**. If you like
GeeksforGeeks and would like to contribute, you can also write an article
using contribute.geeksforgeeks.org or mail your article to
contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks
main page and help other Geeks.

Please write comments if you find anything incorrect, or you want to share
more information about the topic discussed above.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

