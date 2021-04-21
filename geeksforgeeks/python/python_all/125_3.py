Python | Convert nested sublist into tuples



Sometimes, while working with huge amount of data, we might have in which each
point of data constitutes of several elements and needs to be processed as
single unit. For this, we might sometimes, just receive a matrix and it’s
constituent data points are also lists, which don’t make much sense and whole
and might be required to be converted to tuples. Let’s discuss certain ways in
which this task can be performed.

 **Method #1 : Usingtuple() \+ list comprehension**  
This is the one-liner approach to solve this problem. In this we just iterate
through the innermost sublist and convert each of lists to tuple using
tuple().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert nested sublist into tuples

# Using tuple() + list comprehension

 

# Initializing list

test_list = [[[1, 2, 3], [4, 6, 7]], [[6,
9, 8], [10, 11, 12]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert nested sublist into tuples

# Using tuple() + list comprehension

res = [[tuple(ele) for ele in sub] for sub in
test_list]

 

# printing result

print("The data after conversion to tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[[1, 2, 3], [4, 6, 7]], [[6, 9, 8], [10, 11, 12]]]
    The data after conversion to tuple is : [[(1, 2, 3), (4, 6, 7)], [(6, 9, 8), (10, 11, 12)]]
    

**Method #2 : Usingmap() \+ list comprehension + tuple**  
This is another way in which this task can be performed. In this, we reduce
one inner loop and extend the functionality of tuple conversion to each
element using map().

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Convert nested sublist into tuples

# Using map() + list comprehension + tuple

 

# Initializing list

test_list = [[[1, 2, 3], [4, 6, 7]], [[6,
9, 8], [10, 11, 12]]]

 

# printing original list

print("The original list is : " + str(test_list))

 

# Convert nested sublist into tuples

# Using map() + list comprehension + tuple

res = [list(map(tuple, sub)) for sub in test_list]

 

# printing result

print("The data after conversion to tuple is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [[[1, 2, 3], [4, 6, 7]], [[6, 9, 8], [10, 11, 12]]]
    The data after conversion to tuple is : [[(1, 2, 3), (4, 6, 7)], [(6, 9, 8), (10, 11, 12)]]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

