Python unittest – assertNotIn() function



assertNotIn() in Python is a unittest library function that is used in unit
testing to check whether a string is not contained in other. This function
will take three string parameters as input and return a boolean value
depending upon the assert condition. If the key is not contained in container
string it will return true else it returns false.

>  **Syntax:** assertNotIn(key, container, message)
>
>  **Parameters** : assertNotIn() accept three parameters which are listed
> below with explanation:
>
>   *  **key** : a string whose presence is checked in the given container
>   *  **container** : a string in which key string is searched
>   *  **message** : a string sentence as a message which got displayed when
> the test case got failed.
>

Listed below are two different examples illustrating the positive and negative
test case for given assert function:

 **Example 1: Negative Test case**

  

  

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# test suite

import unittest

 

class TestStringMethods(unittest.TestCase):

 # test function to test whether key is present in container

 def test_negative(self):

 key = "geeks"

 container = "geeksforgeeks"

 # error message in case if test case got failed

 message = "key is present in container."

 # assertNotIn() to check if key is in container

 self.assertNotIn(key, container, message)

 

if __name__ == '__main__':

 unittest.main()  
  
---  
  
 __

 __

 **Output:**

    
    
    F
    ======================================================================
    FAIL: test_negative (__main__.TestStringMethods)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/home/e99e85838dde0c8ef29ab17fef478979.py", line 12, in test_negative
        self.assertNotIn(key, container, message)
    AssertionError: 'geeks' unexpectedly found in 'geeksforgeeks' : key is present in container.
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    FAILED (failures=1)

 **Example 2: Positive Test case**

## Python3

 __

 __  
 __

 __

 __  
 __  
 __

# test suite

import unittest

 

 

class TestStringMethods(unittest.TestCase):

 # test function to test whether key is present in container

 def test_positive(self):

 key = "gfgs"

 container = "geeksforgeeks"

 # error message in case if test case got failed

 message = "key is present in container."

 # assertNotIn() to check if key is in container

 self.assertNotIn(key, container, message)

 

 

if __name__ == '__main__':

 unittest.main()  
  
---  
  
 __

 __

 **Output:**

    
    
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s
    
    OK

 **Reference** : https://docs.python.org/3/library/unittest.html

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

