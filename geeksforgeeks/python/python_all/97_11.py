Python | Every Kth element removal in List



We generally wish to employ a particular function to all the elements in a
list. But sometimes, according to requirement we would wish to remove certain
elements of the list, basically to every Kth element in list. Let’s discuss
certain ways in which this can be performed.

 **Method #1 : Using list comprehension +enumerate()**  
The functionality of getting every Kth number of list can be done with the
help of list comprehension and enumerate function helps in the iteration of
the whole list.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Every Kth element removal in List

# using list comprehension + enumerate()

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using list comprehension + enumerate()

# Every Kth element removal in List

# Remove every third element

res = [i for j, i in enumerate(test_list) if j % K
!= 0]

 

# printing result

print ("The list after removing every Kth element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The list after removing every kth element : [4, 5, 7, 8, 12]
    

**Method #2 : Using list comprehension + list slicing**  
Above mentioned functions can help to perform these tasks. The list
comprehension does the task of iteration in list and list slicing does the
extraction of every Kth element.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Every Kth element removal in List

# using list comprehension + list slicing 

 

# initializing list 

test_list = [1, 4, 5, 6, 7, 8, 9, 12]

 

# printing the original list

print ("The original list is : " + str(test_list))

 

# initializing K 

K = 3

 

# using list comprehension + list slicing

# Every Kth element removal in List

# removes every 3rd element

res = [i for i in test_list if i not in test_list[0
:: 3]]

 

# printing result

print ("The list after removing every Kth element : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list is : [1, 4, 5, 6, 7, 8, 9, 12]
    The list after removing every kth element : [4, 5, 7, 8, 12]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

