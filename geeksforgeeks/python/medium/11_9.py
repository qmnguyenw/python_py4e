Python – Itertools.Product()



In the terms of Mathematics Cartesian Product of two sets is defined as the
set of all ordered pairs (a, b) where a belongs to A and b belongs to B.
Consider the below example for better understanding.

 **Examples:**

>  **Input :** arr1 = [1, 2, 3]  
> arr2 = [5, 6, 7]  
>  **Output :** [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3,
> 6), (3, 7)]
>
>  **Input :** arr1 = [10, 12]  
> arr2 = [8, 9, 10]  
>  **Output :** [(10, 8), (10, 9), (10, 10), (12, 8), (12, 9), (12, 10)]

The above solution can be done by looping but we will use a special Python
library **itertools.product()** for finding the Cartesian Product. Let’s go
through the working and use cases of this Python library.

  

  

#### What are Itertools in Python?

Python Itertools is a library in Python which consists of multiple methods
that are used in various iterators to compute a fast and code efficient
solution.

>  _itertools.product() falls under the category calledCombinatoric iterators
> of the Python itertools library._

 **Note:** For more information, refer to Python Itertools

#### What does itertools.product() do?

itertools.product() is used to find the cartesian product from the given
iterator, output is lexicographic ordered. The itertools.product() can used in
two different ways:

*  **itertools.product(*iterables, repeat=1):**  
It returns the cartesian product of the provided itrable with itself for the
number of times specified by the optional keyword “repeat”. For example,
product(arr, repeat=3) means the same as product(arr, arr, arr).

*  **itertools.product(*iterables):**  
It returns the cartesian product of all the itrable provieded as the argument.
For example, product(arr1, arr2, arr3).

 **Example:**

 __

 __  
 __

 __

 __  
 __  
 __

from itertools import product

 

def cartesian_product(arr1, arr2):

 

 # return the list of all the computed tuple

 # using the product() method

 return list(product(arr1, arr2)) 

 

# Driver Function 

if __name__ == "__main__": 

 arr1 = [1, 2, 3]

 arr2 = [5, 6, 7]

 print(cartesian_product(arr1, arr2))  
  
---  
  
 __

 __

 **Output:**

> [(1, 5), (1, 6), (1, 7), (2, 5), (2, 6), (2, 7), (3, 5), (3, 6), (3, 7)]

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

