Python | Difference of two lists including duplicates



The ways to find difference of two lists has been discussed earlier, but
sometimes, we require to remove only the specific occurrences of the elements
as much they occur in other list. Let’s discuss certain ways in which this can
be performed.

 **Method #1 : Usingcollections.Counter()**  
The Counter method can be used to get the exact occurrence of the elements in
the list and hence can subtract selectively rather than using the set and
ignoring the count of elements altogether. Then the subtraction can be
performed to get the actual occurrence.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# Difference of list including duplicates

# Using collections.Counter()

from collections import Counter

 

# initializing lists

test_list1 = [1, 3, 4, 5, 1, 3, 3]

test_list2 = [1, 3, 5]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Using collections.Counter()

# Difference of list including duplicates

res = list((Counter(test_list1) - Counter(test_list2)).elements())

 

# print result

print("The list after performing the subtraction : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [1, 3, 4, 5, 1, 3, 3]
    The original list 2 : [1, 3, 5]
    The list after performing the subtraction : [1, 3, 3, 4]
    

**Method #2 : Usingmap() + lambda + remove()**  
The combination of above functions can be used to perform this particular
task. The map function can be used to link the function to all elements and
remove removes the first occurrence of it. Hence doesn’t remove repeatedly.
Works with Python2 only.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python code to demonstrate

# Difference of list including duplicates

# Using map() + lambda + remove()

 

# initializing lists

test_list1 = [1, 3, 4, 5, 1, 3, 3]

test_list2 = [1, 3, 5]

 

# printing original lists

print("The original list 1 : " + str(test_list1))

print("The original list 2 : " + str(test_list2))

 

# Using map() + lambda + remove()

# Difference of list including duplicates

res = map(lambda x: test_list1.remove(x) 

 if x in test_list1 else None, test_list2)

 

# print result

print("The list after performing the subtraction : " +
str(test_list1))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original list 1 : [1, 3, 4, 5, 1, 3, 3]
    The original list 2 : [1, 3, 5]
    The list after performing the subtraction : [1, 3, 3, 4]
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

