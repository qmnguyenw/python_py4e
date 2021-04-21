Python – Records Maxima in List of Tuples



Sometimes, while working with records, we can have a problem in which we need
to maximum all the columns of a container of lists which are tuples. This kind
of application is common in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingmax() + list comprehension + zip()**  
This task can be performed using combination of above functions. In this, we
cummulate the like index elements, i.e columns using zip(), and then iterate
through them using list comprehension and perform maximum using max().

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Records Maxima in List of Tuples

# using list comprehension + max() + zip()

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Records Maxima in List of Tuples

# using list comprehension + max() + zip()

res = [max(ele) for ele in zip(*test_list)]

 

# printing result

print("The Cummulative column maximum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column maximum is : [6, 7, 8]
    

**Method #2 : Usingzip() + map() + max()**  
This method is similar to the above method. In this, the task performed by
list comprehension is performed by map(), which extends the maximum of columns
to zipped elements.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Records Maxima in List of Tuples

# using zip() + map() + max()

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Records Maxima in List of Tuples

# using zip() + map() + max()

res = list(map(max, zip(*test_list)))

 

# printing result

print("The Cummulative column maximum is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column maximum is : [6, 7, 8]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

