Python | Similarity metrics of strings



This particular utility is quite in demand nowadays due to the similarity
computation requirements in many fields of Computer Science such as Machine
Learning, A.I and web development domains, hence techniques to compute
similarity between any given containers can be quite useful. Let’s discuss
certain ways in which this can be done.

 **Method #1 : Using Naive Approach(sum() + zip())**  
We can perform this particular task using the naive approach, using sum and
zip functions we can formulate a utility function that can compute the
similarity of both the strings.

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# similarity between strings

# using naive method (sum() + zip())

 

# Utility function to compute similarity

def similar(str1, str2):

 str1 = str1 + ' ' * (len(str2) - len(str1))

 str2 = str2 + ' ' * (len(str1) - len(str2))

 return sum(1 if i == j else 0

 for i, j in zip(str1, str2)) / float(len(str1))

 

# Initializing strings

test_string1 = 'Geeksforgeeks'

test_string2 = 'Geeks4geeks'

 

# using naive method (sum() + zip())

# similarity between strings

res = similar(test_string1, test_string2)

 

# printing the result

print ("The similarity between 2 strings is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The similarity between 2 strings is : 0.38461538461538464
    

**Method #2 : UsingSequenceMatcher.ratio()**  
There’s an inbuilt method, that helps to perform this particular task and is
recommended to achieve this particular task as it doesn’t require custom
approach but uses built in constructs to perform task more efficiently.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# similarity between strings

# using SequenceMatcher.ratio()

from difflib import SequenceMatcher

 

# Utility function to compute similarity

def similar(str1, str2):

 return SequenceMatcher(None, str1, str2).ratio()

 

# Initializing strings

test_string1 = 'Geeksforgeeks'

test_string2 = 'Geeks'

 

# using SequenceMatcher.ratio()

# similarity between strings

res = similar(test_string1, test_string2)

 

# printing the result

print ("The similarity between 2 strings is : " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The similarity between 2 strings is :  0.5555555555555556
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

