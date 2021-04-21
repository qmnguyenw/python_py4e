Python | Find missing elements in List



Sometimes, we can get elements in range as input but some values are missing
in otherwise consecutive range. We might have a use case in which we need to
get all the missing elements. Let’s discuss certain ways in which this can be
done.

 **Method #1 : Using list comprehension**  
We can perform the task of finding missing elements using the range function
to get the maximum element fill and then insert the elements if there is a
miss.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Finding missing elements in List

# using list comprehension

 

# initializing list

test_list = [3, 5, 6, 8, 10]

 

# printing original list

print("The original list : " + str(test_list))

 

# using list comprehension

# Finding missing elements in List

res = [ele for ele in range(max(test_list)+1) if
ele not in test_list]

 

# print result

print("The list of missing elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 5, 6, 8, 10]
    The list of missing elements : [0, 1, 2, 4, 7, 9]
    

**Method #2 : Usingset()**  
This problem can also be performed using the properties of difference of set
and then getting the elements that are missing in a range.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Finding missing elements in List

# Using set()

 

# initializing list

test_list = [3, 5, 6, 8, 10]

 

# printing original list

print("The original list : " + str(test_list))

 

# Using set()

# Finding missing elements in List

res = list(set(range(max(test_list) + 1)) -
set(test_list))

 

# print result

print("The list of missing elements : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list : [3, 5, 6, 8, 10]
    The list of missing elements : [0, 1, 2, 4, 7, 9]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

