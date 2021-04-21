Python | Last occurrence of some element in a list



There are many ways to find out the first index of element in the list as
Python in its language provides index() function that returns the index of
first occurrence of element in list. But if one desires to get the last
occurrence of element in list, usually a longer method has to be applied.

Let’s discuss certain shorthands to achieve this particular task.

 **Method #1 : Usingjoin() + rfind()**  
This is usually the hack that we can employ to achieve this task. Joining the
entire list and then employing string function rfind() to get the first
element from right i.e last index of element in list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get last element occurrence

# using join() + rfind()

 

# initializing list

test_list = ['G', 'e', 'e', 'k', 's', 'f',
'o', 'r',

 'g', 'e', 'e', 'k', 's']

 

# using join() + rfind()

# to get last element occurrence

res = ''.join(test_list).rindex('e')

 

# printing result

print ("The index of last element occurrence: " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The index of last element occurrence: 10
    

  
**Method #2 : Using List Slice +index()**  
Using list slicing we reverse the list and use the conventional index method
to get the index of first occurrence of element. Due to the reversed list, the
last occurrence is returned rather than the first index of list.

  

  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get last element occurrence

# using List Slice + index()

 

# initializing list

test_list = ['G', 'e', 'e', 'k', 's', 'f',
'o', 'r',

 'g', 'e', 'e', 'k', 's']

 

# using List Slice + index()

# to get last element occurrence

res = len(test_list) - 1 -
test_list[::-1].index('e')

 

# printing result

print ("The index of last element occurrence: " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The index of last element occurrence: 10
    

  
**Method #3 : Usingmax() + enumerate()**  
We use enumerate function to get the list of all the elements having the
particular element and then max() is employed to get max i.e last index of
the list.  

 __

 __  
 __

 __

 __  
 __  
 __

# Python3 code to demonstrate

# to get last element occurrence

# using max() + enumerate()

 

# initializing list

test_list = ['G', 'e', 'e', 'k', 's', 'f',
'o', 'r',

 'g', 'e', 'e', 'k', 's']

 

# using max() + enumerate()

# to get last element occurrence

res = max(idx for idx, val in enumerate(test_list) 

 if val == 'e')

 

# printing result

print ("The index of last element occurrence: " + str(res))  
  
---  
  
 __

 __

 **Output:**

    
    
    The index of last element occurrence: 10
    

Attention geek! Strengthen your foundations with the **Python Programming
Foundation** Course and learn the basics.

To begin with, your interview preparations Enhance your Data Structures
concepts with the **Python DS** Course.

My Personal Notes _arrow_drop_up_

Save

