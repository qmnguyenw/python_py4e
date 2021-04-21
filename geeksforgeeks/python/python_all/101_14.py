Python – Column Minimum in Tuple list



Sometimes, while working with records, we can have a problem in which we need
to find min of all the columns of a container of lists which are tuples. This
kind of application is common in web development domain. Let’s discuss certain
ways in which this task can be performed.

 **Method #1 : Usingmin() + list comprehension + zip()**  
This task can be performed using combination of above functions. In this, we
cummulate the like index elements, i.e columns using zip(), and then iterate
through them using list comprehension and perform minimum using min().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column Minimum in Tuple list

# using list comprehension + min() + zip()

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Column Minimum in Tuple list

# using list comprehension + min() + zip()

res = [min(ele) for ele in zip(*test_list)]

 

# printing result

print("The Cummulative column minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column minimum is : [1, 2, 3]
    

**Method #2 : Usingzip() + map() + min()**  
This method is similar to the above method. In this, the task performed by
list comprehension is performed by map(), which extends the minimum of columns
to zipped elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column Minimum in Tuple list

# using zip() + map() + min()

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Column Minimum in Tuple list

# using zip() + map() + min()

res = list(map(min, zip(*test_list)))

 

# printing result

print("The Cummulative column minimum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column minimum is : [1, 2, 3]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

