Python | First character occurrence from rear String



There are many ways to find out the first index of element in String as python
in its language provides index() function that returns the index of first
occurrence of element in String. But if one desires to get the last occurrence
of element in string, usually a longer method has to be applied. Lets discuss
certain shorthands to achieve this particular task.

 **Method #1 : Usingrfind()**  
This is usually the hack that we can employ to achieve this task. Employing
string function rfind() to get the first element from right i.e last index of
element in String.

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# First character occurrence from rear String

# using rfind()

 

# initializing string

test_str = "Geeksforgeeks"

 

# printing original string

print ("The original string is : " + str(test_str))

 

# using rfind()

# to get last element occurrence

res = test_str.rfind('e')

 

# printing result

print ("The index of last element occurrence: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeksforgeeks
    The index of last element occurrence: 10
    

**Method #2 : Using List Slice +index() + list()**  
One can convert the string to list using list() and then using list slicing we
reverse the list and use the conventional index method to get the index of
first occurrence of element. Due to reversed list, the last occurrence is
returned rather than the first index of list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python 3 code to demonstrate

# First character occurrence from rear String 

# using List Slice + index() + list()

 

# initializing string

test_str = "Geeksforgeeks"

 

# printing original string

print ("The original string is : " + str(test_str))

 

# using List Slice + index() + list()

# First character occurrence from rear String

test_str = list(test_str)

res = len(test_str) - 1 - test_str[::-1].index('e')

 

# printing result

print ("The index of last element occurrence: " + str(res))  
  
---  
  
 __

 __

 **Output :**

    
    
    The original string is : Geeksforgeeks
    The index of last element occurrence: 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

