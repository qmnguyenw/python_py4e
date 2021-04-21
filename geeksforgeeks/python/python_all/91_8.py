Python | Column Mean in tuple list



Sometimes, while working with records, we can have a problem in which we need
to average all the columns of a container of lists which are tuples. This kind
of application is common in web development domain. Let’s discuss certain ways
in which this task can be performed.

 **Method #1 : Usingsum() + list comprehension + zip()**  
This task can be performed using combination of above functions. In this, we
cummulate the like index elements, i.e columns using zip(), and then iterate
through them using list comprehension and perform summation using sum(). We
divide the each result with No of rows for average computation.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column Mean in tuple list

# using list comprehension + sum() + zip()

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Column Mean in tuple list

# using list comprehension + sum() + zip()

res = [sum(ele) / len(test_list) for ele in
zip(*test_list)]

 

# printing result

print("The Cummulative column mean is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column mean is : [2.6666666666666665, 5.0, 5.666666666666667]
    

**Method #2 : Usingzip() + map() + sum()**  
This method is similar to the above method. In this, the task performed by
list comprehension is performed by map(), which extends the summation of
columns to zipped elements. We divide the each result with No of rows for
average computation.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Column Mean in tuple list

# using zip() + map() + sum()

 

def avg(list):

 return sum(list)/len(list)

 

# initialize list

test_list = [(1, 2, 3), (6, 7, 6), (1, 6,
8)]

 

# printing original list

print("The original list : " + str(test_list))

 

# Column Mean in tuple list

# using zip() + map() + sum()

res = list(map(avg, zip(*test_list)))

 

# printing result

print("The Cummulative column mean is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 2, 3), (6, 7, 6), (1, 6, 8)]
    The Cummulative column mean is : [2.6666666666666665, 5.0, 5.666666666666667]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

