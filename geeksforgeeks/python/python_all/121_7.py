Python | Sort tuple list on basis of difference of elements



Sometimes, while working with data, we can have a problem of sorting them.
There are many types of basis on which sorting can be performed. But this
article discusses sorting on basis of difference of both elements of pair.
Let’s discuss certain ways in which this can be done.

 **Method #1 : Usingsorted() \+ lambda**  
The combination of above functionalities can be used to solve this problem. In
this, sorting is performed by sorted() and lambda function is fed as key to
perform desired sorting.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate working of

# Sort tuple list on basis of difference of elements

# using sorted() + lambda

 

# initialize list 

test_list = [(1, 4), (6, 5), (8, 10)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Sort tuple list on basis of difference of elements

# using sorted() + lambda

res = sorted(test_list, key = lambda sub: abs(sub[1] -
sub[0]))

 

# printing result

print("List after sorting by difference : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 4), (6, 5), (8, 10)]
    List after sorting by difference : [(6, 5), (8, 10), (1, 4)]
    

**Method #2 : Usingsort() + comparator + cmp()**  
This is yet another way to perform this task. In this, we pass the sort(), a
comparator function which performs the similar difference logic using cmp().
Works only in Python2.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate working of

# Sort tuple list on basis of difference of elements

# using sort() + comparator + cmp()

 

# comparator function

def diff_sort(ele1, ele2):

 return cmp(ele2[0] - ele2[1], ele1[0] -
ele1[1])

 

# initialize list 

test_list = [(1, 4), (6, 5), (8, 10)]

 

# printing original list 

print("The original list : " + str(test_list))

 

# Sort tuple list on basis of difference of elements

# using sort() + comparator + cmp()

test_list.sort(diff_sort)

 

# printing result

print("List after sorting by difference : " + str(test_list))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [(1, 4), (6, 5), (8, 10)]
    List after sorting by difference : [(6, 5), (8, 10), (1, 4)]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

