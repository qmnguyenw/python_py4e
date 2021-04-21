Intersection() function Python



 **Intersection** of two given sets is the largest set which contains all the
elements that are **common** to both the sets. Intersection of two given sets
A and B is a set which consists of all the elements which are common to both A
and B.

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/intersection-in-
python.jpg)

 **Examples:**

    
    
    Input: Let set A = {2, 4, 5, 6}
           and set B = {4, 6, 7, 8}
    Output: {4,6} 
    Explanation: Taking the common elements in both the sets,
                 we get {4,6} as the intersection of both the sets.
    

**Syntax:**

> set1.intersection(set2, set3, set4….)  
> In parameters, any number of sets can be given
>
>  
>
>
>  
>

 **Return value:**

> The intersection() function returns a set, which has the intersection of all
> sets(set1, set2, set3…) with set1.  
> It returns a copy of set1 only if no parameter is passed.

Below is the Python3 implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for intersection() function

 

set1 = {2, 4, 5, 6} 

set2 = {4, 6, 7, 8} 

set3 = {4,6,8}

 

# union of two sets

print("set1 intersection set2 : ", set1.intersection(set2))

 

# union of three sets

print("set1 intersection set2 intersection set3 :",
set1.intersection(set2,set3))  
  
---  
  
 __

 __

 **Output:**

    
    
    set1 intersection set2 :  {4, 6}
    set1 intersection set2 intersection set3 : {4, 6}
    

**Practical applications** :  
In most of the probability problems, the concept of intersection of sets is
needed.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

