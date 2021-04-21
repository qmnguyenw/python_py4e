Python Program to Sort the list according to the column using lambda



Given a list, the task is to sort the list according to the column using the
lambda approach.

 **Examples:**

>  **Input :**  
>  array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]]  
>  **Output :**  
>  Sorted array specific to column 0, [[1, 3, 3], [2, 1, 2], [3, 2, 1]]  
> Sorted array specific to column 1, [[2, 1, 2], [3, 2, 1], [1, 3, 3]]  
> Sorted array specific to column 2, [[3, 2, 1], [2, 1, 2], [1, 3, 3]]
>
>  **Input :**  
>  array = [[‘java’, 1995], [‘c++’, 1983], [‘python’, 1989]]  
>  **Output :**  
>  Sorted array specific to column 0, [[‘c++’, 1983], [‘java’, 1995],
> [‘python’, 1989]]  
> Sorted array specific to column 1, [[‘c++’, 1983], [‘python’, 1989],
> [‘java’, 1995]]

 **Approach:**

  

  

  * sorted() built-in function in Python gives a new sorted list from an iterable.
  * key parameter to specify a function to be called on each list element prior to making comparisons.
  * lambda is used as a function to iterate on each element.
  * key = lambda x:x[i] here i is the column on which respect to sort the whole list.

Below is the implementation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to sorting list

# according to the column

 

# sortarray function is defined

def sortarray(array):

 

 for i in range(len(array[0])):

 

 # sorting array in ascending 

 # order specific to column i,

 # here i is the column index

 sortedcolumn = sorted(array, key = lambda x:x[i])

 

 # After sorting array Column 1

 print("Sorted array specific to column {}, \

 {}".format(i, sortedcolumn))

 

# Driver code 

if __name__ == '__main__': 

 

 # array of size 3 X 2 

 array = [['java', 1995], ['c++', 1983],

 ['python', 1989]]

 

 # passing array in sortarray function

 sortarray(array)  
  
---  
  
 __

 __

 **Output:**

> Sorted array specific to column 0, [[‘c++’, 1983], [‘java’, 1995],
> [‘python’, 1989]]  
> Sorted array specific to column 1, [[‘c++’, 1983], [‘python’, 1989],
> [‘java’, 1995]]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

