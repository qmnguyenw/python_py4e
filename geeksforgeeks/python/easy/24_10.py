Union() function in Python



 **Union** of two given sets is the smallest set which contains all the
elements of both the sets. Union of two given sets A and B is a set which
consists of all the elements of A and all the elements of B such that no
element is repeated.

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Union-in-
python.jpg)

The symbol for denoting union of sets is **‘U’**  
 **Examples:**

    
    
    Input:Let set A = {2, 4, 5, 6}
          and set B = {4, 6, 7, 8}
    Output: {2, 4, 5, 6, 7, 8} 
    Explanation: Taking every element of both the sets A and B, 
                 without repeating any element, we get a 
                 new set = {2, 4, 5, 6, 7, 8}.This new set 
                 contains all the elements of set A and all the elements 
                 of set B with no repetition of elements and is 
                 named as union of set A and B.  
    

**Syntax:**

> set1.union(set2, set3, set4….)  
> In parameters, any number of sets can be given
>
>  
>
>
>  
>

 **Return value:**

> The union() function returns a set, which has the union of all sets(set1,
> set2, set3…) with set1.  
> It returns a copy of set1 only if no parameter is passed.

Below is the Python3 implementation of the above approach:

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 program for union() function

 

set1 = {2, 4, 5, 6} 

set2 = {4, 6, 7, 8} 

set3 = {7, 8, 9, 10}

 

# union of two sets

print("set1 U set2 : ", set1.union(set2))

 

# union of three sets

print("set1 U set2 U set3 :", set1.union(set2, set3))  
  
---  
  
 __

 __

 **Output:**

    
    
    set1 U set2 :  {2, 4, 5, 6, 7, 8}
    set1 U set2 U set3 : {2, 4, 5, 6, 7, 8, 9, 10}
    

**Practical applications** :

In most of the probability problems, the concept of union of sets is needed.

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

