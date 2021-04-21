Difference between List and Array in Python



 **List:** A list in Python is a collection of items which can contain
elements of multiple data types, which may be either numeric, character
logical values, etc. It is an ordered collection supporting negative indexing.
A list can be created using [] containing data values.  
Contents of lists can be easily merged and copied using python’s inbuilt
functions.

 __

 __  
 __

 __

 __  
 __  
 __

# creating a list containing elements

# belonging to different data types

sample_list = [1,"Yash",['a','e']]

print(sample_list)  
  
---  
  
 __

 __

 **Output :**

    
    
    [1, 'Yash', ['a', 'e']]
    

The first element is an integer, the second a string and the third is an list
of characters.

 **Array:** An array is a vector containing homogeneous elements i.e.
belonging to the same data type. Elements are allocated with contiguous memory
locations allowing easy modification, that is, addition, deletion, accessing
of elements. In Python, we have to use the array module to declare arrays.
If the elements of an array belong to different data types, an exception
“Incompatible data types” is thrown.

 __

 __  
 __

 __

 __  
 __  
 __

# creating an array containing same

# data type elements 

import array

 

sample_array = array.array('i', [1, 2, 3]) 

 

# accessing elements of array

for i in sample_array:

 print(i)  
  
---  
  
 __

 __

 **Output :**

  

  

    
    
    1
    2
    3
    

Here are the differences between List and Array in Python :List| Array| Can
consist of elements belonging to different data types| Only consists of
elements belonging to the same data type| No need to explicitly import a
module for declaration| Need to explicitly import a module for declaration|
Cannot directly handle arithmetic operations| Can directly handle arithmetic
operations| Can be nested to contain different type of elements| Must contain
either all nested elements of same size| Preferred for shorter sequence of
data items| Preferred for longer sequence of data items| Greater flexibility
allows easy modification (addition, deletion) of data| Less flexibility since
addition, deletion has to be done element wise| The entire list can be printed
without any explicit looping| A loop has to be formed to print or access the
components of array| Consume larger memory for easy addition of elements|
Comparatively more compact in memory size  
---|---  
  
Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

