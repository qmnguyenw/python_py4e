Python | Convert column to separate elements in list of lists



There are instances in which we might require to extract a particular column
of a Matrix and assign its each value as separate entity in list and this
generally has a utility in Machine Learning domain. Let’s discuss certain ways
in which this action can be performed.

 **Method #1 : Using list slicing and list comprehension**  
The functionality of list slicing and comprehension can be clubbed to perform
the particular task of extracting a column from a list and then it can be
added as new element using list comprehension.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# column to separate elements in list of lists

# using list slicing and list comprehension

 

# initializing list of list 

test_list = [[1, 3, 4],

 [6, 2, 8],

 [9, 10, 5]]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using list slicing and list comprehension

# column to separate elements in list of lists

res = [i for nest_list in [[j[1 : ], [j[0]]]

 for j in test_list] for i in nest_list]

 

# printing result

print ("The list after colum shift is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[1, 3, 4], [6, 2, 8], [9, 10, 5]]
    The list after colum shift is : [[3, 4], [1], [2, 8], [6], [10, 5], [9]]
    

**Method #2 : Usingitertools.chain() \+ list comprehension + list slicing**  
The above method can be improved by inducing the concept of element chaining
and reduce the overhead of the list comprehension and reducing the time taken
to execute this particular task.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# column to separate elements in list of lists

# using itertools.chain()+ list comprehension + list slicing

from itertools import chain

 

# initializing list of list 

test_list = [[1, 3, 4],

 [6, 2, 8],

 [9, 10, 5]]

 

# printing original list 

print ("The original list is : " + str(test_list))

 

# using itertools.chain() + list comprehension + list slicing

# column to separate elements in list of lists

res = list(chain(*[list((sub[1: ], [sub[0]]))

 for sub in test_list]))

 

# printing result

print ("The list after colum shift is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[1, 3, 4], [6, 2, 8], [9, 10, 5]]
    The list after colum shift is : [[3, 4], [1], [2, 8], [6], [10, 5], [9]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

